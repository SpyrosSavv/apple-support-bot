import pytest

from app.config import Settings

TEST_JWT_SECRET = "test-secret-that-is-at-least-32-characters-long"


@pytest.fixture
def settings() -> Settings:
    """Settings for tests: no .env file, fast retries, no real services."""
    return Settings(
        _env_file=None,
        JWT_SECRET=TEST_JWT_SECRET,
        HTTP_RETRY_BASE_WAIT_SECONDS=0,
        BREAKER_FAIL_MAX=3,
        INCLUDE_TRACE_IN_RESPONSE=True,
    )
