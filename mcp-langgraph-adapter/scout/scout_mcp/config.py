"""
This file loads required secrets from the .env file into the mcp_config.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
import json


load_dotenv()


def resolve_env_vars(config: dict) -> dict:
    for server_name, server_config in config["mcpServers"].items():
        for property in server_config.keys():
            if property == "env":
                for key, value in server_config[property].items():
                    if isinstance(value, str) and value.startswith("${"):
                        env_var_name = value[2:-1]
                        env_var_value = os.environ.get(env_var_name, None)
                        if env_var_value is None:
                            raise ValueError(f"Environment variable {env_var_name} is not set")
                        config["mcpServers"][server_name][property][key] = env_var_value
            if property == "args":
                for i, arg in enumerate(server_config[property]):
                    if isinstance(arg, str) and arg.startswith("${"):
                        env_var_name = arg[2:-1]
                        env_var_value = os.environ.get(env_var_name, None)
                        if env_var_value is None:
                            raise ValueError(f"Environment variable {env_var_name} is not set")
                        config["mcpServers"][server_name][property][i] = env_var_value
    return config


# get the path to the mcp_config.json file
config_file = Path(__file__).parent / "mcp_config.json"
if not config_file.exists():
    raise FileNotFoundError(f"mcp_config.json file {config_file} does not exist")

with open(config_file, "r") as f:
    config = json.load(f)


# instead of directly using config.json, we open the config.json file, and get its configuration which is dict. Now, the configuration in config.json need environment variables from .env file, so we add the environment variables in the configuration dict object and then we will use that.
mcp_config = resolve_env_vars(config)['mcpServers']

