from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # --- Secrets ---
    JWT_SECRET: str = Field(min_length=32)
    JWT_ALGORITHM: str = "HS256"
    GOOGLE_API_KEY: str = ""
    OPENAI_API_KEY: str = ""

    # --- LangSmith tracing ---
    LANGSMITH_TRACING: bool = False
    LANGSMITH_API_KEY: str = ""
    LANGSMITH_PROJECT: str = "apple-support-bot"

    # --- Service URLs ---
    GPTCACHE_URL: str = "http://localhost:8001"
    ATTACK_DETECTOR_URL: str = "http://localhost:8002"
    MONGODB_URI: str = "mongodb://localhost:27017"
    MONGODB_DB: str = "support_bot"
    POSTGRES_DSN: str = "postgresql://postgres:postgres@localhost:5432/support_bot"

    # --- Models ---
    LOW_COMPLEXITY_MODEL: str = "gemini-3.5-flash"
    HIGH_COMPLEXITY_MODEL: str = "gemini-3.1-pro"
    ROUTER_MODEL: str = "gemini-3.5-flash"
    COMPLETENESS_JUDGE_MODEL: str = "gemini-3.5-flash"
    FAITHFULNESS_JUDGE_MODEL: str = "gpt-4o-mini"
    LLM_TIMEOUT_SECONDS: float = 60.0
    LLM_MAX_RETRIES: int = 2

    # --- Prompts ---
    PROMPT_VERSION: str = "v1"

    # --- Request limits ---
    MAX_INPUT_CHARS: int = 4000
    RATE_LIMIT: str = "30/minute"

    # --- Session memory ---
    MAX_SESSION_TURNS: int = Field(default=10, ge=1)
    PROMPT_HISTORY_TURNS: int = Field(default=3, ge=0)

    # --- Retrieval ---
    DOC_ID: str = "apple-support"
    DOC_TREE_CACHE_SECONDS: int = 300

    # --- Safety ---
    ATTACK_DETECTOR_FAIL_OPEN: bool = False

    # --- Answer checks (0 to 1) ---
    FAITHFULNESS_THRESHOLD: float = Field(default=0.7, ge=0, le=1)
    COMPLETENESS_THRESHOLD: float = Field(default=0.6, ge=0, le=1)

    # --- Semantic cache ---
    CACHE_ENABLED: bool = True

    # --- Resilience ---
    HTTP_RETRY_ATTEMPTS: int = 3
    HTTP_RETRY_BASE_WAIT_SECONDS: float = 0.5
    BREAKER_FAIL_MAX: int = 5
    BREAKER_RESET_SECONDS: int = 30

    # --- Logging & debugging ---
    LOG_LEVEL: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = "INFO"
    INCLUDE_TRACE_IN_RESPONSE: bool = False


@lru_cache
def get_settings() -> Settings:
    return Settings()
