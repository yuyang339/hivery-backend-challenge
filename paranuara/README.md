
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

## TODO
- more unittest
- list fruits used in helpers/common.py
- list vegetables used in helpers/common.py
- API documentation