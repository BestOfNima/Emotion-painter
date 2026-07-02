import os
from faster_whisper import WhisperModel

AUDIO_FOLDER = "audio"

model = WhisperModel(
    "medium",
    device="cpu",
    compute_type="int8"
)


def transcribe(filename, language="en"):
    filepath = os.path.join(AUDIO_FOLDER, filename)

    if not os.path.exists(filepath):
        raise FileNotFoundError(filepath)

    segments, info = model.transcribe(
        filepath,
        language=language
    )

    text = ""

    for segment in segments:
        text += segment.text

    return text.strip()