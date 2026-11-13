import pytest
from pydantic import ValidationError

from app.config import Settings


def test_missing_jwt_secret_is_rejected(monkeypatch):
    monkeypatch.delenv("JWT_SECRET", raising=False)
    with pytest.raises(ValidationError):
        Settings(_env_file=None)


def test_short_jwt_secret_is_rejected():
    with pytest.raises(ValidationError):
        Settings(_env_file=None, JWT_SECRET="change-me-in-prod")


def test_env_vars_override_defaults(monkeypatch):
    monkeypatch.setenv("JWT_SECRET", "x" * 32)
    monkeypatch.setenv("LOW_COMPLEXITY_MODEL", "my-model")
    assert Settings(_env_file=None).LOW_COMPLEXITY_MODEL == "my-model"


def test_max_session_turns_must_be_positive():
    # history[-0:] would keep the whole history, the opposite of what 0 suggests
    with pytest.raises(ValidationError):
        Settings(_env_file=None, JWT_SECRET="x" * 32, MAX_SESSION_TURNS=0)
