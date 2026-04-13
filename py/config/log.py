LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(levelprefix)s %(message)s",
            "use_colors": None,
        },
        "rich": {
            "format": "%(message)s",
            "datefmt": "[%X]",
        },
        "detailed": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "rich.logging.RichHandler",
            "formatter": "rich",
            "rich_tracebacks": True,
            "markup": True,
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "detailed",
            "filename": "app.log",
            "maxBytes": 1000000,  # 1MB
            "backupCount": 5,
        },
    },
    "loggers": {
        "uvicorn": {"handlers": ["console", "file"], "level": "INFO"},
        "uvicorn.error": {"handlers": ["console", "file"], "level": "INFO"},
        "uvicorn.access": {"handlers": ["console", "file"], "level": "INFO", "propagate": False},
        "app": {"handlers": ["console", "file"], "level": "DEBUG", "propagate": False},
    },
}