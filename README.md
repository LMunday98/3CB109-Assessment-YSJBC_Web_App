# 3CB109-Assessment-WebAppREST

## About
This assignment requires the development of a REST web service application. A client and server will be developed and hosted on CS2S. A read me document will need to be produced, detailing how to run and install the application.


## Requirements
* The code should contain at least a client, a server and one service.

* The service needs to be provided by a database that is also hosted on cs2s.

* The service must be written in Python. The client in html / javascript.

## Project Stucture

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

│   │   │   │   │   ├── logo.jpg

│   │   │   │   │   ├── row_main.jpeg

│   │   │   │   │   ├── scull.jpg

│   │   │   │   │   └── YSJ.svg

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

│   ├── run.py

└── README.md
