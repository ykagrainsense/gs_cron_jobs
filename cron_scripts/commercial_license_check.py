"""
commercial_license_check
Calls the configured license check endpoint and returns the HTTP status code and request duration.
"""
import os

from .utils import get_env, timed_get


def main():
    server_token = get_env("AUTHORIZED_SERVER_TOKEN", required=True)
    server_url_default = os.getenv("SERVER_URL")
    url = get_env("LICENSE_CHECK_URL", default=server_url_default, required=True)
    headers = {"X-Authorized-Server-Token": server_token}

    response, duration = timed_get(url, headers=headers)

    return {
        "status_code": response.status_code,
        "request_time_seconds": duration,
    }


if __name__ == "__main__":
    import json
    import sys

    try:
        result = main()
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc

    print(json.dumps(result))
