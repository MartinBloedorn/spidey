# spidey
A web crawler. Ergo the name. See? Spidey? Got it? ... Sorry. I'm leaving. 

# What's the point? 
A scraping that gathers information from articles on [Gizmodo US](http://us.gizmodo.com), saves them to a DB and serves the info through a REST API. 

**spidey** is now running on [`martinvb.com/spidey`](http://martinvb.com/spidey). Load the page's JSON response into a [viewer](http://codebeautify.org/jsonviewer#), if you wish. 

# Dependencies and setup
*Spidey* depends on [*django*](https://www.djangoproject.com/), [*django-rest-framework*](http://www.django-rest-framework.org) and [*scrapy*](http://www.scrapy.org). To get them (with [*pip*](https://pypi.python.org/pypi/pip)):

    pip install django
    pip install djangorestframework
    pip install scrapy
    
Alternatively, you may use the supplied `requirements.txt` file to install the dependencies, by running:

    pip install -r path/to/spidey/requirements.txt
    
Note that *scrapy* depends on [*lxml*](http://lxml.de/). **pip** will run the required compilation/installation, but the compilation may fail on machines with 512MB of RAM (as it did on my VPS). If that's the case, add a swap file as nicely detailed [here](http://stackoverflow.com/questions/18334366/out-of-memory-issue-in-installing-packages-on-ubuntu-server). 

After installing the deps, get this repo with:

    git clone https://github.com/MartinBloedorn/spidey.git

To ensure that the directory is writable (specially the **sqlite** database), execute:

    sudo chown -R $USER:$USER spidey/
    sudo chmod -R 755 spidey/
    
To get it up and running (with **sqlite**), execute: 

    cd spidey
    python manage.py makemigrations     # creates initialization files for the db
    python manage.py migrate            # initializes the tables on the db
    python manage.py runserver          # fires the app up
  
Gets the server running on `localhost:8000` (by default). 

## Configuring it with Apache
By default, **spidey** (i.e., **django**) listens on `localhost:8000`. If **spidey** is on a VPS running **Apache** that hosts `example.com`, you may want to redirect `example.com/spidey` to `localhost:8000` - making **spidey**'s API available on that URL (some useful info is available [here](https://www.digitalocean.com/community/tutorials/how-to-set-up-apache-virtual-hosts-on-ubuntu-14-04-lts)).

To do so, edit the `example.com` configuration file (may be `example.com.conf`, or by default `000-default.conf`), usually under `/etc/apache2/sites-enabled`. In the file, add the following lines to the definition of the *VirtualHost*: 

    <VirtualHost *:80>
        # ...
        # Add the lines below:
        ProxyPass /spidey http://127.0.0.1:8000
        ProxyPassReverse /spidey http://127.0.0.1:8000
    </VirtualHost>

Make sure the following modules are loaded into **Apache** (using `a2enmod`):    

    mod_proxy
    mod_proxy_http
    mod_ssl
    
Restart **Apache** (in Debian-based systems: `sudo service apache2 restart`). Good to go! 

## Configuring *crontab*
To have the crawler run every second hour, one simple solution is to add it as a **cron** job. 

In the **spidey** repo, `launch_crawler.sh` calls the crawler. Mark it as executable with `chmod a+x launch_crawler.sh`. Add it as a **cron** job. Run:

    crontab -e

In the editor, add the following line:

    * */2 * * * /path/to/spidey/launch_crawler.sh
    
The `* */2 * * *` part sets the script to be executed every two hours. 

## Poor man's automatic deployment
Though platforms such as [Heroku](http://heroku.com) and [DeployBot](http://deploybot.com) exist to enable decent automatic deployments, a simple/crippled/fairly-dumb alternative can be scripted directly into Git's hooks. 

Let's start by hosting a **spidey** repo on the target VPS (intersting info on that [here](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-private-git-server-on-a-vps)). Suppose 
a user `johndoe`:

    johndoe@vps $ cd ~ 
    johndoe@vps $ git clone --bare https://github.com/MartinBloedorn/spidey.git spidey-bare  

The `--bare` options makes a full copy of the repo, enabling it to be *pushed* to. To easily access the HEAD version of **spidey** however, let's add a local repository tracking this local *bare* repo:

    johndoe@vps $ git clone spidey-bare spidey      # clones a regular repo off of spidey-bare
    
Everytime `spidey-bare` receives a *push*, it may run various hooks (callbacks, if you will). We're interested in the `post-update` callback. To make **git** run it, execute:

    mv spidey-bare/hooks/post-update.sample spidey-bare/hooks/post-update
    chmod a+x spidey-bare/hooks/post-update
    
With your editor of choice, edit `spidey-bare/hooks/post-update` to look like:

    # Inside a Hook, git repos are '.', but we'll temporarily set them to '.git'
    GIT_DIR='.git'
    # Store the current working directory, to return to it
    CWD="$(pwd)"
    # Fuser kills the process on port 8000; in this case, python/django
    fuser -k 8000/tcp 
    # Go to the local spidey repo (not spidey-bare)
    cd /home/johndoe/spidey 
    # Get the changes pushed to the bare repo
    git pull origin 
    # Setup and run the server
    cd spidey
    python manage.py makemigrations 
    python manage.py migrate
    python manage.py runserver &
    # Undo changes 
    cd $CWD
    GIT_DIR='.'
    # Return info about the push to the user (if you skip this line, `git push deploy` will hang)
    exec git update-server-info
    # Exit script 
    exit 0

Needles to say, this script is dumb and is as robust as a castle of cards on a plane's wing. It's just a bare-minimum starting point for a simple automatic deployment for **spidey**. Logging and checking are welcome. 

Lastly, in the repository on its local machine, `johndoe` needs to add the path to `spidey-bare`. Suppose the VPS hosts `example.com`:

    johndoe@local $ git remote add deploy johndoe@example.com:spidey-bare
    
Now, local modifications can be pushed to the server and automaticaly deployed (theoretically) with

    johndoe@local $ git push deploy 

# Structure of this tool

## REST
The REST portion of this tool is implemented using the **django-rest-framework**, which sits on top of the **django** framework. 

## Scraper
The scraper/crawler is implemented using the **scrapy** framework. 

