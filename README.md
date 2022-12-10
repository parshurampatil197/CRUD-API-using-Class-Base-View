

## CRUD API using Class Base View

<br/>


# Description

I have created CRUD API with SQLite database that uses Django Rest Framework for building Rest 
API. 
DRF allows us to work with class based views.
I have implementd Django class based view for the Restful Web service. 

<br/>

# Requirements

Last tested successfully with Python 3.6.19 and Ubuntu 16.04
Django==3.1.1\
djangorestframework==3.12.4


[Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).

[DRF](https://github.com/gitgik/django-rest-api/blob/master/www.django-rest-framework.org): A powerful and flexible toolkit for building Web APIs


<br/>

# Quick Setup

1. Create a folder for your project on your local machine
```bash
  mkdir myproject; 
  cd myproject
```

2. Create a virtual environment and install django

```bash
  virtualenv venv --python=python3 ; 
  source venv/bin/activate; 
```

3.  Install the dependencies needed to run the app:
```bash
  pip install -r requirements. txt 
```

4. Download this project template from GitHub
```bash
  git clone https://github.com/parshurampatil197/CRUD-API-using-Class-Base-View.git
  cd CRUD-API-using-Class-Base-View
```

5. Initialize the database
```bash
  python manage.py makemigrations
  python manage.py migrate
```

6. Run the project
```bash
  python manage.py runserver
```

<br/>

# API Reference
 
Test API by Using POSTMAN
#### Http request: POST 

```http
  http://127.0.0.1:8000/studentapi/
```

#### Request

```http
 {
    "name" : "Parshuram",
    "roll" : 101,
    "city": "Pune",
    
}
```
#### Http request: GET 

```http
  http://127.0.0.1:8000/studentapi/
```

```http
  http://127.0.0.1:8000/studentapi/?id=1
```


#### Response

```http
{
    "name" : "Parshuram",
    "roll" : 101,
    "city": "Pune",
    
}
```

#### Http request: PUT 

```http
  http://127.0.0.1:8000/studentapi/2
```

#### Http request: DELETE 

```http
  http://127.0.0.1:8000/studentapi/3
```



## Authors

- [@parshuram](https://github.com/parshurampatil197)

