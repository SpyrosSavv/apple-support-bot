import logging

import structlog


def configure_logging(level: str = "INFO") -> None:
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.JSONRenderer(),
        ],
        wrapper_class=structlog.make_filtering_bound_logger(logging.getLevelName(level)),
        context_class=dict,
        logger_factory=structlog.PrintLoggerFactory(),
        cache_logger_on_first_use=True,
    )


def bind_request_context(**fields: object) -> None:
    """Replace the per-request logging context (call at the start of each request)."""
    structlog.contextvars.clear_contextvars()
    structlog.contextvars.bind_contextvars(**fields)


def get_logger(**fields: object) -> structlog.typing.FilteringBoundLogger:
    return structlog.get_logger().bind(**fields)
