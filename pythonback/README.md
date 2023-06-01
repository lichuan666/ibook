# reverseSys

## How To Create project in local

### 1. Install mysql database
- install mysql database
- create database and user, the config is in reverseSys/settings.py DATABASES
### 2. Install dependencies
- pip install -r requirements.txt
### 3. Enter the project, execute the following command in the terminal
- python manage.py makemigrations
- python manage.py migrate
- python manage.py init_data
### 4. Start the project
- python manage.py runserver 127.0.0.1:8080

## Er Diagram
https://www.processon.com/view/link/6436730eaffa5b5bb8ce8bde

## edit database
### alter table
edit login\models.py
### insert data
edit login\management\commands\init_data.py