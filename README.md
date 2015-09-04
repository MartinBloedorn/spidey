# spidey
A web crawler. Ergo the name. See? Spidey? Got it? ... Sorry. I'm leaving. 

# What's the point? 
A scraping that gathers information from articles on [Gizmodo US](http://us.gizmodo.com), saves them to a DB and serves the info through a REST API. 

**spidey** is now running on `martinvb.com/spidey`. Load the page's JSON response into a [viewer](http://codebeautify.org/jsonviewer#), if you wish. 

# Dependencies and setup
*Spidey* depends on [*django*](https://www.djangoproject.com/), [*django-rest-framework*](http://www.django-rest-framework.org) and [*scrapy*](http://www.scrapy.org). To get them (with [*pip*](https://pypi.python.org/pypi/pip)):

    pip install django
    pip install djangorestframework
    pip install scrapy
    
Note that *scrapy* depends on [*lxml*](http://lxml.de/). **pip** will run the required compilation/installation, but the compilation may fail on machines with 512MB of RAM (as it did on my VPS). If that's the case, add a swap file as nicely detailed [here](http://stackoverflow.com/questions/18334366/out-of-memory-issue-in-installing-packages-on-ubuntu-server). 

After installing the deps, get this repo with:

    git clone https://github.com/MartinBloedorn/spidey.git
    
To get it up and running (with **sqlite**), execute: 

    cd spidey
    python manage.py migrate      # initializes the tables on the db
    python manage.py runserver    
  
Gets the server running on `localhost:8000` (by default). 

# Configuring it with Apache
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

# Structure of this tool

## REST
The REST portion of this tool is implemented using the **django-rest-framework**, which sits on top of the **django** framework. 

## Scraper
The scraper/crawler is implemented using the **scrapy** framework. 

