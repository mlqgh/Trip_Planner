import yaml
import os

def load_config(config_path:str='config/config.yaml')-> dict:
    """
    Load the configuration from a YAML file.

    Args:
        config_path (str): Path to the YAML configuration file.

    Returns:
        dict: The loaded configuration.
    """
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config