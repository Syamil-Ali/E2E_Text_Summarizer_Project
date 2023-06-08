import os
from pathlib import Path # get path
import logging # to log information

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# provide project name
project_name = "textSummerizer"

# list file need to create
list_of_files = [
    ".github/workflows/.gitkeep", # for ci/cd
    f"src/{project_name}/__init__.py", # constructor file
    f"src/{project_name}/components/__init__.py", # constructor file
    f"src/{project_name}/utils/__init__.py", # constructor file
    f"src/{project_name}/utils/common.py", # constructor file
    f"src/{project_name}/logging/__init__.py", # constructor file
    f"src/{project_name}/config/__init__.py", # constructor file
    f"src/{project_name}/config/configuration.py", # constructor file
    f"src/{project_name}/pipeline/__init__.py", # constructor file
    f"src/{project_name}/entity/__init__.py", # constructor file
    f"src/{project_name}/constants/__init__.py", # constructor file
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f'Creating empty file: {filepath}')
    
    else:
        logging.info(f'{filename} is already exists')



