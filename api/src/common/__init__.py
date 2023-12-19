import os

from .config import Settings

env = os.environ["ENV"]
base_dir = os.environ["BASE_DIR"]

settings = Settings()
