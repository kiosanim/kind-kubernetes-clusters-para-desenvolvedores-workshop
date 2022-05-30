import os
from pydantic import BaseSettings
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


class CommonSettings(BaseSettings):
    PORT: int = int(os.getenv("PORT", "5000"))
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "develop")


class RoutesSettings(BaseSettings):
    PROSPECTS_ROUTE: str = os.getenv("PROSPECTS_ROUTE", "/prospects")


class Environment(CommonSettings,
                  RoutesSettings):
    pass


APP_ENVIRONMENT = Environment()