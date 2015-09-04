# spidey
A web crawler. Ergo the name. See? Spidey? Got it? ... Sorry. I'm leaving. 

# What's the point? 
A scraping that gathers information from articles on [Gizmodo US](http://us.gizmodo.com), saves them to a DB and serves the info through a REST API. 

# Dependencies and setup
*Spidey* depends on [*django*](https://www.djangoproject.com/), [*django-rest-framework*](http://www.django-rest-framework.org) and [*scrapy*](http://www.scrapy.org). To get them (with [*pip*](https://pypi.python.org/pypi/pip)):

    pip install django
    pip install djangorestframework
    pip install scrapy
    
Note that *scrapy* depends on [*lxml*](http://lxml.de/). **pip** will run the required compilation/installation, but the compilation may fail on machines with 512MB of RAM (e.g., as it did on my server). If that's the case, add a swap file as nicely detailed [here](http://stackoverflow.com/questions/18334366/out-of-memory-issue-in-installing-packages-on-ubuntu-server). 

After installing the deps, get this repo with:

    git clone https://github.com/MartinBloedorn/spidey.git
    
To get it up and running (with **sqlite**), execute: 

    cd spidey
    python manage.py migrate      # initializes the tables on the db
    python manage.py runserver    
  
Gets the server running on `localhost:8000` (by default). 

# Structure of this tool

## REST
The REST portion of this tool is implemented using the **django-rest-framework**, which sits on top of the **django** framework. 

## Scraper
The scraper/crawler is implemented using the **scrapy** framework. 

