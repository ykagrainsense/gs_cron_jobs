import os
import time

import requests

DEFAULT_TIMEOUT_SECONDS = float(os.getenv("REQUEST_TIMEOUT_SECONDS", "120"))


def get_env(name, default=None, required=False):
    value = os.getenv(name, default)
    if required and (value is None or value == ""):
        raise ValueError(f"Missing required environment variable: {name}")
    return value


def timed_get(url, headers=None, timeout_seconds=None):
    timeout = DEFAULT_TIMEOUT_SECONDS if timeout_seconds is None else timeout_seconds
    start_time = time.time()
    response = requests.get(url, headers=headers, timeout=timeout)
    duration = time.time() - start_time
    return response, duration
