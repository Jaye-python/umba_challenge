# umba_challenge
Repo to submit umba challenge

<!-- STAGE 1 -->
seed.py has been created with option to indicate number of users to seed the database. There is an option below the code that prints the database objects that are seeded just for confirmation and debugging

On windows, these are the commands:
1. To automatically seed the database with default first 150 users use (and get it printed on the console):
    python seed.py

2. To seed the database with any number of users you choose use (and get it printed on the console):
    python seed.py -t <number>
    python seed.py --total <number>
    
    
    
<!-- STAGE 2 -->
seed_extended file is now uploaded with configurations to seed POSTGRES DB

Django project is used for the application. db password required
    
Following commands are required:
    django-admin startproject umbaproject
    django-admin startapp github
    ****Register 'github' under list of INSTALLED_APPS in settings.py****
    
    pip install psycopg2
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    
URLS:
    http://127.0.0.1:8000/
    http://127.0.0.1:8000/users/?page=2
    http://127.0.0.1:8000/users/?pagination=3
    
    
    
<!--   STAGE 3 -->
    pip install django-rest-framework
****Register 'rest_framework' under list of INSTALLED_APPS in settings.py****
    
API URLS:
    http://127.0.0.1:8000/api/users/profiles/
    http://127.0.0.1:8000/api/users/profiles/id/<id>
    http://127.0.0.1:8000/api/users/profiles/username/<username>

 order_by condition is already programmed in models.py
    
    

    
    
    
    
  




