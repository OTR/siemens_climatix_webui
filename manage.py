#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main(path_to_settings: str) -> None:
    """
    Run administrative tasks.

    :param path_to_settings: which django settings use (test, production, etc).
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', path_to_settings)
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # Try to look up for setting in environment variable first
    # If not set use test settings
    env_django_settings = os.environ.get(
        "DJANGO_SETTINGS_MODULE",
        "config.settings.test_settings"
    )
    main(env_django_settings)
