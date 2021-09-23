import os
from typing import Dict, Literal, get_args
from dotenv import load_dotenv

load_dotenv()

EnvName = Literal["ACCESS_TOKEN", "REPO", "TAG_NAME"]


def read_env(name: str) -> str:
    value = os.environ.get(name)

    if value is None:
        raise Exception(f"environment variable {name} is not set")

    return value


envs: Dict[EnvName, str] = dict(
    map(lambda envName: (envName, read_env(envName)), get_args(EnvName))
)
