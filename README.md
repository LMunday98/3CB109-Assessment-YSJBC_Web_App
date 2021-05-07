# 3CB109-Assessment-YSJBC_Web_App

## About

This assignment requires the development of a REST web service application. A client and server will be developed and hosted on CS2S. A read me document will need to be produced, detailing how to run and install the application.

## Project Specification

* The code should contain at least a client, a server and one service.

* The service needs to be provided by a database that is also hosted on cs2s.

* The service must be written in Python. The client in html / javascript.

## Installation and Setup

1. Begin by cloning the repository to your local machine

2. Ensure all the required modules documented in 'project/requirements.txt' are installed

3. Check the connection settings in 'project/run.py' and 'project/app/\_\_init\_\_.py'

   Eg: If running locally, set the connection ip and port in run.py to '0.0.0.0:5000' and the sqlaclhemy database URI to 'mysql://root:''@127.0.0.1/flask'
   
   This assumes a mysql database has been initalised with the name 'flask'
   
4. Run the 'project/models.py' script to migrate and seed the database

5. Run the 'project/run.py' script to start the flask web server and connect using the ip and port number defined in step 2

## Deafult User Accounts

### Admin Account
Email: luke@admin

Password: LukePass

Permissions: Create, Read, Update and Delete

### Admin Account
Email: mike@admin

Password: Mike

Permissions: Create, Read, Update and Delete

### User Account
Email: user@gmail.com

Password: user

Permissions: Read

### Unauthorised Guest Account
Email: guest@gmail.com 

Password: guest

Permissions: Read (Limited to public content)

## Project Features

### Admin

* If the user logins in with an admin account, they will have the option to CRUD blogs and timetable events.
* They also have the option to approve newly registered guest accounts into user accounts, so they can access the user site.

### User

* Once an admin has approved an account, the user will then be able to login and view the currently scheduled events.

### System

* The site is seperated into three tiers of permission levels, meaning certain account types only have access to pages of their permission level.
  1. Public
  2. User
  3. Admin

### Blogs

* The admins have the ability to create blog posts, where the three most recently published posts will appear on the home page.

### Events

* Admins also have the ability to schedule events for reistered users to see.
* They can choose from multiple activity types and have the option to set the exact date, start time and end time.

## Links

GitHub:
https://github.com/LMunday98/3CB109-Assessment-YSJBC_Web_App

README:
https://github.com/LMunday98/3CB109-Assessment-YSJBC_Web_App/blob/main/README.md

## Project Structure
``` bash
3CB109-Assessment-WebAppREST/
├── .gitignore
├── project/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── controllers/
│   │   │   ├── __init__.py
│   │   │   ├── auth_controller.py
│   │   │   ├── blog_controller.py
│   │   │   ├── event_controller.py
│   │   │   └── user_manager.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── blog.py
│   │   │   ├── event.py
│   │   │   └── user.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── api.py
│   │   │   └── web.py
│   │   ├── static/
│   │   │   ├── assets/
│   │   │   │   ├── css/
│   │   │   │   │   ├── contact.css
│   │   │   │   │   ├── home.css
│   │   │   │   │   ├── main.css
│   │   │   │   │   ├── template.css
│   │   │   │   │   └── timetable.css
│   │   │   │   ├── images/
│   │   │   │   │   ├── carousel/
│   │   │   │   │   │   ├── row_main.jpeg
│   │   │   │   │   │   ├── scull.jpg
│   │   │   │   │   │   ├── scull2.jpeg
│   │   │   │   │   │   └── sweep1.jpeg
│   │   │   │   │   ├── featured_photos/
│   │   │   │   │   │   ├── alex_scull.jpg
│   │   │   │   │   │   ├── men_carry.jpg
│   │   │   │   │   │   ├── teach_scull.jpg
│   │   │   │   │   │   └── women_carry.jpg
│   │   │   │   │   ├── iconCol.png
│   │   │   │   │   └── logo.jpg
│   │   │   │   ├── js/
│   │   │   │   │   └── gmaps.js
│   │   │   │   └── scss/
│   │   │   ├── blog_thumbnails/
│   │   │   │   ├── blog1.jpg
│   │   │   │   ├── blog2.jpg
│   │   │   │   ├── blog3.jpg
│   │   │   │   └── blog4.jpg
│   │   │   └── seed_thumbnails/
│   │   │       ├── blog1.jpg
│   │   │       ├── blog2.jpg
│   │   │       ├── blog3.jpg
│   │   │       └── blog4.jpg
│   │   └── templates/
│   │       ├── admin/
│   │       │   ├── blog.html
│   │       │   ├── home.html
│   │       │   ├── training.html
│   │       │   └── user_manager.html
│   │       ├── auth/
│   │       │   ├── login.html
│   │       │   └── register.html
│   │       ├── base.html
│   │       ├── components/
│   │       │   ├── blog/
│   │       │   │   ├── blog_form.html
│   │       │   │   ├── blog_rows.html
│   │       │   │   ├── blog_tile.html
│   │       │   │   └── blog_view.html
│   │       │   ├── events/
│   │       │   │   ├── event_form.html
│   │       │   │   └── timetable.html
│   │       │   ├── nav/
│   │       │   │   ├── nav_bar.html
│   │       │   │   └── nav_links.html
│   │       │   └── user_management/
│   │       │       └── create_button.html
│   │       ├── public/
│   │       │   ├── about.html
│   │       │   ├── blog.html
│   │       │   ├── contact.html
│   │       │   └── index.html
│   │       └── user/
│   │           ├── home.html
│   │           └── training.html
│   ├── config.py
│   ├── models.py
│   ├── requirements.txt
│   └── run.py
└── README.md
```
