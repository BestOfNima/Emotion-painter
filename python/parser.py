import json
import re


def _extract_json_block(text: str) -> str:
    """
    Best-effort extraction of a JSON object from a raw LLM response.

    Local models don't always obey "return ONLY JSON" - they may wrap the
    object in ```json fences, or add a leading/trailing sentence. This pulls
    out the outermost {...} block so json.loads has a fighting chance.
    """

    cleaned = text.strip()

    fence_match = re.search(r"```(?:json)?\s*(.*?)```", cleaned, re.DOTALL)
    if fence_match:
        cleaned = fence_match.group(1).strip()

    if not cleaned.startswith("{"):
        start = cleaned.find("{")
        end = cleaned.rfind("}")
        if start != -1 and end != -1 and end > start:
            cleaned = cleaned[start:end + 1]

    return cleaned


def _normalize_emotion_dna(dna) -> dict:
    """Lowercase all keys and coerce values to numbers, dropping bad entries."""

    if not isinstance(dna, dict):
        return {}

    normalized = {}

    for key, value in dna.items():
        try:
            normalized[str(key).strip().lower()] = float(value)
        except (TypeError, ValueError):
            normalized[str(key).strip().lower()] = 0

    return normalized


def _normalize_colors(colors) -> list:
    """Ensure colors is always a list of strings, even if the model
    returned a single comma-separated string like "Yellow, Orange"."""

    if isinstance(colors, list):
        return [str(c).strip() for c in colors if str(c).strip()]

    if isinstance(colors, str):
        return [c.strip() for c in colors.split(",") if c.strip()]

    return []


def parse_response(response: str) -> dict:
    """
    Parse an Ollama JSON response.

    Returns a dictionary with safe default values, tolerant of common
    small-model quirks (markdown fences, stray prose, wrong casing/types).
    """

    from python.constants import DEFAULT_RESPONSE
    defaults = DEFAULT_RESPONSE.copy()

    if not response or not response.strip():
        return defaults

    try:
        cleaned = _extract_json_block(response)
        data = json.loads(cleaned)

        if not isinstance(data, dict):
            return defaults

        defaults.update(data)

        defaults["emotion_dna"] = _normalize_emotion_dna(defaults.get("emotion_dna"))
        defaults["colors"] = _normalize_colors(defaults.get("colors"))
        defaults["dominant_emotion"] = str(defaults.get("dominant_emotion") or "Unknown").strip()
        defaults["style"] = str(defaults.get("style") or "").strip()
        defaults["prompt"] = str(defaults.get("prompt") or "").strip()

        return defaults

    except Exception:

        return defaults
