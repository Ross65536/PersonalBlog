# Personal Website 

A Website that I have built for myself to display my resume and blog on the web. Some HTML knowledge is needed to modify the contents of the pages. 

## Installation

#### To run locally:

1. Install python v3.5 or higher and pip
2. Run pip install -r requirements.txt
3. Set the following environment variables (which are used in django's PersonalWebsite/settings.py file):
    - DEBUG (optional): only set this if you want debug information, leave unset to disable debugging.
    - SECRET_KEY: the private key used by django.
    - DATABASE_URL: url to the database following the [dj-database-url format](https://github.com/kennethreitz/dj-database-url/blob/master/README.rst)
4. Run python manage.py runserver
5. Open localhost:8000 in your browser.

## Personalization

You can modify the variables in personalPages/values.py to display your own name, email, etc.
You can also modify personalPages/resume.html to add some personal information about yourself inside the "block body" 

### Features

The blog feature is not implemented yet.

The style follows the [Tomorrow Night](https://github.com/chriskempson/tomorrow-theme) color scheme