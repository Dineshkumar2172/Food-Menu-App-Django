# Food-Menu-App-Django

## Project Structure

```
       /mysite
        |_ /mysite
            |_ __init__.py
            |_ asgi.py
            |_ settings.py
            |_ urls.py
            |_ wsgi.py

        |_ manage.py
```

```manage.py``` - command line utility to perform administrative tasks and interacting with our django project. This convenience means that any command run using python manage.py is executed within the context of your specific Django project, with all its configurations (database, installed apps, etc.) readily available. 

```\_\_init\_\_.py``` -  to mark the inner mysite directory as a python package - marking it as a package facilitates importing of codes written inside this directory into other code.

```settings.py``` - contains all settings for our django project. it's the main configuration for our django project.

```wsgi.py``` - web server gateway interface - it acts as an entry point for deploying our application. it's used for deploying our application.

```asgi.py``` - asynchronous server gateway interface - it's similar to wsgi but it's used for handling async web protocols like websockets.

```urls.py``` - contains all the URL patterns that are required inside our application.

## Django Components

```urls``` - maps web addresses (URLs) to Python functions called views

```views``` - functions contains business logic to process the incoming request and send back response.

```Models``` - it is a blueprint which is used to create database tables and interact with them without having to write SQL. Model is a python class. Models are defined in models.py file.
