# BrainApp

# How to run the project ?

    $ git clone <url_repo>
    
# Create Database
    
    $ mysql -u root -p
    $ create database <db_name>
    $ GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'localhost';

# Migrate data to the database

    $ python manage.py makemigrations
    $ python manage.py migrate
    $ python manage.py runserver