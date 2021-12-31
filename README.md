# umba_challenge
Repo to submit umba challenge

STAGE 1
seed.py has been created with option to indicate number of users to seed the database. There is an option below the code that prints the database objects that are seeded just for confirmation and debugging

On windows, these are the commands:
1. To automatically seed the database with default first 150 users use (and get it printed on the console):
    python seed.py

2. To seed the database with any number of users you choose use (and get it printed on the console):
    python seed.py -t <number>
    python seed.py --total <number>
    
    
    
STAGE 2
seed_extended file is now uploaded with configurations to seed POSTGRES DB

Django project is used for the application. db password required
    
Following steps and commands are required to start the app from scratch:
    django-admin startproject umbaproject
Copy contents of 'urls_main.py' into the 'urls.py' file that was auto-created by Django
    
    django-admin startapp github
    
Create 'urls.py' file in the newly created github app
Copy contents of 'urls.py' into this newly created file
    
Register 'github' under list of INSTALLED_APPS in settings.py
****provide a password for the database****
    
    pip install psycopg2
    python manage.py makemigrations
    python manage.py migrate
    
Copy content of files: views.py, urls.py, settings.py
Create folder under github titled 'templates', under 'templates' create another folder titled 'github' then drop 'base.html' and 'home.html' in the folder (i.e. github folder)
Create folder under github titled 'static', under 'static' create another folder titled 'github' then drop 'ss.css' in the folder (i.e. github folder)
    
    python manage.py runserver
    
URLS:
    http://127.0.0.1:8000/
    http://127.0.0.1:8000/users/?page=2
    http://127.0.0.1:8000/users/?pagination=3
    
    
    
STAGE 3
    pip install django-rest-framework
****Register 'rest_framework' under list of INSTALLED_APPS in settings.py****
    
API URLS:
    http://127.0.0.1:8000/api/users/profiles/
    http://127.0.0.1:8000/api/users/profiles/id/<id>
    http://127.0.0.1:8000/api/users/profiles/username/<username>

 order_by condition is already programmed in models.py
    
    

    
    
    
    
  




