
# Smarte Benutzeroberfläche 
### Für Anwendungen künstlicher Intelligenz in komplexen Fertigungslinen

<br />

Features of the Django Datta Able Dashboard Template

- `Up-to-date dependencies`
- Database: 'sqlite'
- UI-Ready app, Django Native ORM
- `Session-Based authentication`, Forms validation
- Bootstrap 4 Lite Admin Template

## Integrierte KI Anwendungen
- Qualitätsvorhersage
- Bildanalyse


<br />

<br />

##  How to use it

> Download the code
```bash
$ # Get the code
$ git clone https://github.com/Moltrosaurus/MA-Django-Template.git
$ cd django-datta-able

```

<br />

### Set Up for `Unix`, `MacOS`

> Install modules via 'VENV'

```bash
$ virtualenv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Database
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> Start the app
```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`.

<br />

###  Set Up for `Windows` 

> Install modules via `VENV` (windows) 
```
$ virtualenv env
$ .\env\Scripts\activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Database
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> Start the app
```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

###  Create Users

By default, the app redirects guest users to authenticate. In order to access the private pages, follow this set up: 

- Start the app via `django run`
- Access the `registration` page and create a new user:
  - `http://127.0.0.1:8000/register/`
- Access the `sign in` page and authenticate
  - `http://127.0.0.1:8000/login/`

<br />

##  Code-base structure

The project is coded using a simple and intuitive structure presented below:

```bash
< PROJECT ROOT >
   |
   |-- core/                               # Implements app configuration
   |    |-- settings.py                    # Defines Global Settings
   |    |-- wsgi.py                        # Start the app in production
   |    |-- urls.py                        # Define URLs served by all apps/nodes
   |
   |-- apps/
   |    |
   |    |-- home/                          # A simple app that serve HTML files
   |    |    |-- views.py                  # Serve HTML pages for authenticated users
   |    |    |-- urls.py                   # Define some super simple routes  
   |    |
   |    |-- qualityend/                          # App für Qualitätsvorhersage
   |    |    |-- views.py                  # Serve HTML pages for authenticated users
   |    |    |-- urls.py                   # Define some routes  
   |    |
   |    |-- authentication/                # Handles auth routes (login and register)
   |    |    |-- urls.py                   # Define authentication routes  
   |    |    |-- views.py                  # Handles login and registration  
   |    |    |-- forms.py                  # Define auth forms (login and register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |         |-- includes/                 # HTML chunks and components
   |         |    |-- navigation.html      # Top menu component
   |         |    |-- sidebar.html         # Sidebar component
   |         |    |-- footer.html          # App Footer
   |         |    |-- scripts.html         # Scripts common to all pages
   |         |
   |         |-- layouts/                   # Master pages
   |         |    |-- base-fullscreen.html  # Used by Authentication pages
   |         |    |-- base.html             # Used by common pages
   |         |
   |         |-- accounts/                  # Authentication pages
   |         |    |-- login.html            # Login page
   |         |    |-- register.html         # Register page
   |         |
   |         |-- home/                      # UI Kit Pages
   |              |-- index.html            # Index page
   |              |-- 404-page.html         # 404 page
   |              |-- *.html                # All other pages
   |
   |-- datasets                             # Rohdaten für ML Anwendung
   |
   |-- Notebooks/                            # Beinhaltet .ipynb ML Datei 
   |    |-- .csv                            # Defines Global Settings
   |    |-- quality_prediction.ipynb        # Code Qualitätsvorhersage
   |    |-- tree_regressor.pkl              # Trained ML Model
   |
   |-- requirements.txt                     # Development modules - SQLite storage
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- manage.py                            # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />

## How to start the app in Docker

> **Step 1** - Download the code from the GH repository (using 'GIT')

```bash
$ # Get the code
$ git clone https://github.com/Moltrosaurus/MA-Django-Template.git 
$ cd ?
```

<br />

> **Step 2** - Edit `.env` and remove or comment all `DB_*` settings (`DB_ENGINE=...`). This will activate the `SQLite` persistance. 
```txt
DEBUG=True
# Deployment SERVER address
SERVER=.appseed.us
# For MySql Persistence
# DB_ENGINE=mysql            <-- REMOVE or comment for Docker
# DB_NAME=appseed_db         <-- REMOVE or comment for Docker  
# DB_HOST=localhost          <-- REMOVE or comment for Docker 
# DB_PORT=3306               <-- REMOVE or comment for Docker
# DB_USERNAME=appseed_db_usr <-- REMOVE or comment for Docker
# DB_PASS=<STRONG_PASS>      <-- REMOVE or comment for Docker
```

<br />

> **Step 3** - Start the APP in Docker

```bash
$ docker-compose up --build 
```

Visit `http://localhost:5085` in your browser. The app should be up & running.

<br />

##  Credits & Links

### [What is Django](https://docs.appseed.us/content/what-is/django)

[Django](https://www.djangoproject.com/) is a Python-based free and open-source web framework, which follows the model-template-view architectural pattern. 
It is maintained by the Django Software Foundation, an independent organization established as a 501 non-profit. Django's primary goal is to ease the creation of complex, database-driven websites.

<br />

### What is a dashboard

A dashboard is a set of pages that are easy to read and offer information to the user in real-time regarding his business. 
A dashboard usually consists of graphical representations of the current status and trends within an organization. 
Having a well-designed dashboard will give you the possibility to act and make informed decisions based on the data that your business provides 
- *definition provided by [Creative-Tim - Free Dashboard Templates](https://www.creative-tim.com/blog/web-design/free-dashboard-templates/?ref=appseed)*.

<br />

### Datta Able Free Dashboard

Datta Able Bootstrap Lite is the most styled Bootstrap 4 Lite Admin Template, around all other Lite/Free admin templates in the market. It comes with high feature-rich pages and components with fully developer-centric code. 
Comes with error/bug-free, well structured, well-commented code and regularly with all latest updated code, which saves your large amount of developing backend application time and it is fully customizable. 
Provided by **CodedThemes**.

Open-source **Django Dashboard** generated by `AppSeed` op top of a modern design. 
**[Datta Able](https://appseed.us/generator/datta-able/)** 
Bootstrap Lite is the most stylised Bootstrap 4 Lite Admin Template, around all other Lite/Free admin templates in the market. 
It comes with high feature-rich pages and components with fully developer-centric code. 
Before developing Datta Able our key points were performance and design.

<br />
**Free [Support](https://appseed.us/support/)** (registered users) via `Email` and `Discord`


---
[Datta Able](https://appseed.us/generator/datta-able/) Django - Open-source starter generated by **[AppSeed Generator](https://appseed.us/generator/)**.
