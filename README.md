# DRFToken

Behold My Awesome Project!

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT


## Basic Commands

### Setting Up Your Users

-   To create a **superuser account**, use this command:

        $ python manage.py createsuperuser

## How to run it:

Start Postrgresql: 

On lixux:
        
        sudo su postgres
        psql

Rise a database called : drftoken

        CREATE DATABASE drftoken WITH OWNER postgres ENCODING 'UTF8';
        GRANT ALL PRIVILEGES ON DATABASE drftoken TO postgres;

Start a virtual environment, go to the project folder and run:

        pip install -r requeriments/local.py

Migrate

        python3 manage.py migrate

Create a Superuser:

        python3 manage.py createsuperuser

Run the server and have fun on http://localhost:8000 !:

        python3 manage.py runserver


Use Postman to send a HTTP POST Request with body content:

                KEY             VALUE
                username        <yoursuperuser>
                password        <yoursuperuserpass>

to:

                http://localhost:8000/api/v1/