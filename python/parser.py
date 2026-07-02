import json


def parse_response(response: str) -> dict:
    """
    Parse Ollama JSON response.

    Returns a dictionary with safe default values.
    """

    from python.constants import DEFAULT_RESPONSE
    defaults = DEFAULT_RESPONSE.copy()

    try:

        data = json.loads(response)

        if not isinstance(data, dict):
            return defaults

        defaults.update(data)

        return defaults

    except Exception:

        return defaults