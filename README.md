
# IGS Employee Manager

The app "IGS Employee Manager"  it has:

* A dashboard on the Django admin site for managing employee and department data
* A Django API with methods::
    * List, add and remove employees
    * List, add and remove departments

* A page with all employees and departments listed in a table




## Comments
I developed the functions using generic classes, as the requirements are simple and did not require the creation of specific methods, and to meet the requirements of returning the department name in the employee's request, I created two serializers to be able to create and display the data correctly

## Installation

create a virtual environment

```
  python -m venv venv
```
Install install the requirements

 ```
    pip install -r requirements.txt
 ```

clone the github repository

```
  git clone https://github.com/Saviodiow95/IGSEmployeeManager.git
```

open the project folder and start the server
```
    cd IGSEmployeeManager

    python manage.py runserver
```

run the migrations
```
    python manage.py migrate
```

create a super user

```
    python manage.py createsuperuser
```

## public website

click [here](http://127.0.0.1:8000/) to access the public page with the list of employees and departments, in the url http://127.0.0.1:8000/


## API examples

### Request

```
curl -H "Content-Type: application/javascript" http://localhost:8000/employee/
```

### Return

```
[
  {
    "name": "Jose da Silva",
    "email": "jose.silva@igs-software.com.br",
    "department": "Tester"
  },
  {
    "name": "Jose dos Santos",
    "email": "jose.santos@igs-software.com.br",
    "department": "Developer"
  },
  {
    "name": "Jose Lima",
    "email": "jose.lima@igs-software.com.br",
    "department": "RH"
  }
]
```


### Request

```
curl -H "Content-Type: application/javascript" http://localhost:8000/department/
```

### Return

```
[
  {
    "name": "Tester",
    "description": "Equipe especializada em realizar testes nos sistemas criados pela Equipe de Desenvolvimento"
  },
  {
    "name": "Developer",
    "description": "Equipe de criação e manutenção dos sistemas da empresa"
  },
  {
    "name": "RH",
    "description": "Equipe que cuida da gestão dos funcionarios da empresa"
  }
]
```