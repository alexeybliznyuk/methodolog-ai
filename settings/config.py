import os, sys
from functools import cached_property
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import ValidationError
import requests

# from errors.orm import ConfigFileNotFound
# from utils.request import AsyncRequest

project_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
sys.path.append(project_directory)
print(project_directory)
if os.path.exists(f"{project_directory}/.env"):
    global_env = f"{project_directory}.env"
    help_service_env = f"{project_directory}/global/services/help-service.env"


else:
    global_env = "/app/settings/.env"
    help_service_env = "/app/settings/help-service.env"


class GlobalSettings(BaseSettings):

    COURSE_STRUCTURE_AI_NETWORK: str
    COURSE_STRUCTURE_AI_PORT: int

    model_config = SettingsConfigDict(env_file=global_env)





global_settings = GlobalSettings()




class Settings(BaseSettings):
    COURSE_STRUCTURE_AI_API_KEY: str 
    COURSE_STRUCTURE_AI_REQUESTS_URL: str 

    model_config = SettingsConfigDict(env_file=help_service_env)



settings = Settings()