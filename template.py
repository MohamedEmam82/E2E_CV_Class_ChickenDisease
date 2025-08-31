import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,
                    format="[%(asctime)s]: %(message)s:")

project_name = "ChickenDisease"

list_of_files = [
    ".github/workflows/.gitkeep",  # .gitkeep is a dummy file to keep the folder in github repo, because git doesn't
                                   # track empty folder. later we will add yaml file for CI/CD, "cicd.yaml"
                                   
    f"src/{project_name}/__init__.py",

    f"src/{project_name}/components/__init__.py",

    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common_functions.py",

    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",

    f"src/{project_name}/pipeline/__init__.py",

    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",

    f"src/{project_name}/constants/__init__.py",

    #f"src/{project_name}/logging/__init__.py", # logging logic code will be written in..
                                                # "src/wine_quality/__init__.py" for simplicity.
    "config/config.yaml",
    "params.yaml",
    #"schema.yaml",                             # Not needed for this project. It's used for tabular data in ML.
    #".gitignore",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(name=filedir, exist_ok=True)
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(msg=f"Creating empty file {filepath}")
    else:
        logging.info(msg=f"{filename} does already exsit!")