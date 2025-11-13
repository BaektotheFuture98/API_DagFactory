from dagfactory import load_yaml_dags
from pathlib import Path
import os

DEFAULT_CONFIG_ROOT_DIR = "/mnt/c/Users/sun44/vscode/DagFactory/dags"
CONFIG_ROOT_DIR = Path(os.getenv("CONFIG_ROOT_DIR", DEFAULT_CONFIG_ROOT_DIR))

config_file = str(CONFIG_ROOT_DIR/"basic_example.yml")

load_yaml_dags(
    globals_dict=globals(),
    config_filepath=config_file
)