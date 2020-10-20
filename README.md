# Welcome to the Product Purchasing Web App!

This readme file contains the following information:
- Details on the architecture and components of the application
- Instructions for setting the development environment
- Instructions for migrating and running the application

# App Architecture
----

Below is a description of the different components of this project

| Component | Description | Project Path | URL (local) |
| ------ | ------ | ------ | ------ |
| Frontend | I built the UI using basic Dango templates | /frontend | http://www.localhost.com:8000/ | 
| Backend | I built the api using the Django REST framework | /products | http://www.localhost.com:8000/products |  http://www.localhost.com:8000/admin | 
| Database | I used a basic/local sqlite database for this project | /db.sqlite3 |  |  
| Admin  | I built on the Django admin module to manage the dataset | /products/admin.py |
| Fixtures | I created fixtures to load initial data to the database | /fixtures |  |  
| Unit Tests | I created a couple of unit tests using the REST framework class | /products/tests.py |  | 


# Development Environment Setup
----

#### Assumption: Python 3 is installed
I used python 3.8 to build the application. This guide assumes that you have Python 3 and the pip package installed on your machine

#### Assumption: Visual Studio Code is installed
I used Visual Studio Code to develop the application. Other IDEs (such as PyCharm) may be used, but they have not been tested.

#### Clone the source code from GitHub
The complete source code is available in GitHub and can be cloned into a local folder:
```sh
git clone https://github.com/vbasantes/productpurchase_project.git
```

#### Dependency Management
I used the pipenv tool to manage the virtual environment and theseproject dependencies (via Pipfile and Pipfile.lock). You will need pipenv installed on your machine:
```sh
pip install pipenv
```
Currently, the application has the following dependencies: rest framework, requests, CHANGEME

# Setting up the app
----

### Setup virtual environment
The application manages dependencies in a virtual environment using pipenv. 

Run the following command to create a virtual environment and install all dependencies:
```sh
pipenv install
```

Active the virtual environment:
```sh
pipenv install
```

### Run the database migrations
The application includes migrations to create all tables in the database. This includes all the models and their associations. Run the migrations:
```sh
python manage.py migrate
```

### Load initial data 
The application includes fixtures to load dummy product data. This is useful  as it creates a dataset of products ready to be ordered. Load the fixtures into the database:
```sh
python manage.py loaddata fixtures/initial_data.json
```

### Create an admin user to manage dataset
The application is setup to use the Django admin site for managing the dataset. Create an admin user to make data management accessible:
```sh
python manage.py createsuperuser
```

### Run the application
Finally, run the Django web application on port 8000:
```sh
python manage.py runserver 8000
```