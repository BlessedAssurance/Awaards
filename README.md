# Awaards

## Description
Awaards is a social web application that allows users to upload their projects and see other user's projects. Visit the live site on https://blessedawaards.herokuapp.com/

## Author
* [**Kirui Vincent**](https://github.com/BlessedAssurance)

## Features

* As a user you will be able to:
1. Register in the application
2. Sign In
3. Post your projects link
4. Post project Images
5. Rate other users projects

## Setup & Installations

1. Git clone the repository: * https://github.com/BlessedAssurance/Awaards

2. Extract and open in vs code or any IDE of your choice

3. On your root folder create a virtual environment

4. Install requirements 
    
    $ pip install -r requirements.txt

5. Create a Database on your terminal 

 $ CREATE DATABASE db_name;

6. On the terminal make migrations

* $ python manage.py makemigrations ('app_name')

7. Run the migrations 

* $ python manage.py migrate

8. Serve the application by running:

* $ python manage.py runserver


## Technologies Used
- Python3.6
- Django 2
- Postgresql

## License

[![License:MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](license/MIT)
