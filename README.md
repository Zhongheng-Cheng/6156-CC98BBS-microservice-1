# 6156-microservice-1

Simple starter template from [Professor's template project](https://github.com/donald-f-ferguson/e6156-f23-template).

## Directory Structure

### Folders and files

- `data/`: json files containing data

- `resources/`: supportive python scripts
    - `entityxxx`: the entity in the microservice structure
        - `xxx_data_service`: a class that understands how to connect to an external database and get data in and out of the database. (Eventually it will connect to database, but for now it reads data from `./data/xxx.json`.)
        - `xxx_resources`: a interface to data_service.
        - `xxx_models`: the data objects that can go back and forth in OpenAPI. (also define attributes here)

- `static/`: html files

- `tts/`: test cases
    - It contains test cases for every xxx_data_service and xxx_resource in `./resources/`.

- `main.py` is the python application launched to start the web service. 
    - also implement paths here.

- The `.gitignore` file is the default for python from GitHub and prevents pushing the virtual environment and python-related files into the repo.

### Python Virtual Environment

- Using a `python virtual environment` is a best practice.

- This projects virtual environment is in `venv`.