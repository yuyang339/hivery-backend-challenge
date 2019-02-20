
*NOTE:*
Always running command under `hivery-backend-chanllenge/paranuara`.

# Getting Set Up:
- `python3 -m venv paranuara_venv`
- `source activate`

# Installing packages:
- ensure you are in the `paranuara_venv` virtualenv (run `. activate` if not)
- run `pip install -e .` to install all dependencies

# Running Mongod service:
- ensure you have the Mongod service running

# Running migration at the first time
- `python paranuara/helpers/migration.py` which will load ../../resources/company.json and ../../resources/people.json data to database `paranuara`

# Running the Project:
- provisioning your local mongodb host/port in config.yaml before running the project
- `paranuara`

# Running tests:
- `pytest tests`

# API
## 1. Company API
### 1.1 Get all employees
```
GET /api/company/{company_id}/employees
```
### Description
Given a company id, this API returns all the employees.


## 2. People API
### 2.1 Get a list of fruits and vegetables
 ```
GET /api/people/{people_id}/favoritefood
```
### Description
Given a people id, this API returns a list of fruits and vegetables.


## 3. Common Friends API
### 3.1 Get people information and common friends
 ```
GET /api/people/{people_aid}/{people_bid}
```
### Description
Given 2 people, provide their information (Name, Age, Address, phone) and the list of their friends in common

### 3.2 Get people information and common friends which have brown eyes and are still alive
 ```
GET /api/people/{people_aid}/{people_bid}?isalive=true&eyecolor=brown
```

### Description
Given 2 people, provide their information (Name, Age, Address, phone) and the list of their friends in common which have brown eyes and are still alive.



# TODO
- more unittest
- support more HTTP methods 
