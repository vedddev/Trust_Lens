from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    ai_api_key: str = ""
    ai_base_url: str = ""
    ai_model: str = ""
    frontend_url: str = "http://localhost:5173"
    request_timeout_seconds: float = 6.0
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

@lru_cache
def get_settings() -> Settings:
    return Settings()
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    ai_api_key: str = ""; ai_base_url: str = ""; ai_model: str = ""
    frontend_url: str = "http://localhost:5173"; request_timeout_seconds: float = 6.0
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
@lru_cache
def get_settings() -> Settings: return Settings()
from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    ai_api_key: str = ''; ai_base_url: str = ''; ai_model: str = ''
    frontend_url: str = 'http://localhost:5173'; request_timeout_seconds: float = 6.0
    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

@lru_cache
def get_settings() -> Settings: return Settings()
