import sys
import logging
import structlog

logging.basicConfig(level=logging.INFO)

shared_processors = [
    structlog.stdlib.add_log_level,
    structlog.stdlib.add_logger_name,
    structlog.processors.TimeStamper(fmt="iso", utc=True),
    structlog.processors.StackInfoRenderer()
]

if sys.stdout.isatty():
    # Pretty print in an interactive terminal
    shared_processors.append(structlog.dev.ConsoleRenderer())
else:
    # Log as JSON (common in Docker or non-TTY environments)
    shared_processors.append(structlog.processors.JSONRenderer())

structlog.configure(
    processors=shared_processors,
    context_class=dict,
    logger_factory=structlog.stdlib.LoggerFactory(),
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

logger = structlog.get_logger("TatiGPT")
