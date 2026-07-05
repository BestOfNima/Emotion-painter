import os
import uuid
from datetime import datetime

import streamlit as st

from python.app_STT import transcribe
from python.app_ollama import generate_prompt
from python.app_image import I2M
from python.parser import parse_response
from python.styles import inject_css
from python.ui import (
    render_prompt,
    render_summary,
    render_emotions,
    render_debug,
    render_download,
)

# ───────────────────────────────────────────────────────────────
# Page config
# ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Emotion Painter",
    page_icon="🎙️",
    layout="centered",
)

os.makedirs("audio", exist_ok=True)

inject_css()

# ───────────────────────────────────────────────────────────────
# Session State
# ───────────────────────────────────────────────────────────────
if "text_content" not in st.session_state:
    st.session_state.text_content = ""

if "last_audio_id" not in st.session_state:
    st.session_state.last_audio_id = None

if "current_audio_filename" not in st.session_state:
    st.session_state.current_audio_filename = None

if "result" not in st.session_state:
    st.session_state.result = None

if "last_generated_text" not in st.session_state:
    st.session_state.last_generated_text = None

# ───────────────────────────────────────────────────────────────
# Title
# ───────────────────────────────────────────────────────────────
st.markdown("# 🎙️ Emotion Painter")
st.markdown(
    '<p class="section-subtitle">Record or write · detect the emotion · paint it</p>',
    unsafe_allow_html=True,
)

# ==============================================================
# AUDIO
# ==============================================================

st.markdown("""
<div class="section-card">
<div class="section-title">🎤 Record Audio</div>
<div class="section-subtitle">Press the microphone button to record.</div>
</div>
""", unsafe_allow_html=True)

audio_value = st.audio_input(
    "Tap to record",
    label_visibility="collapsed",
)

if audio_value is not None:

    current_id = id(audio_value)

    if st.session_state.last_audio_id != current_id:

        filename = (
            f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_"
            f"{uuid.uuid4().hex[:8]}.mp3"
        )

        st.session_state.last_audio_id = current_id
        st.session_state.current_audio_filename = filename

        path = os.path.join("audio", filename)

        with open(path, "wb") as f:
            f.write(audio_value.getvalue())

        with st.spinner("Transcribing..."):
            transcript = transcribe(filename)

        st.session_state.text_content = transcript

    st.markdown(
        f'<div class="saved-badge">Saved : audio/{st.session_state.current_audio_filename}</div>',
        unsafe_allow_html=True,
    )

    st.audio(audio_value)

# ==============================================================
# Saved recordings
# ==============================================================

st.markdown("#### 📁 All recordings")

files = sorted(
    [
        f
        for f in os.listdir("audio")
        if f.endswith((".mp3", ".wav"))
    ],
    reverse=True,
)

if files:

    for file in files:
        st.caption(file)
        st.audio(os.path.join("audio", file))

else:

    st.caption("No recordings.")

# ==============================================================
# TEXT
# ==============================================================

st.markdown("""
<div class="section-card">
<div class="section-title">✍️ Write Text</div>
<div class="section-subtitle">Write anything or use speech-to-text.</div>
</div>
""", unsafe_allow_html=True)

text = st.text_area(
    "Text",
    value=st.session_state.text_content,
    height=180,
    label_visibility="collapsed",
)

st.session_state.text_content = text

char_count = len(text)
word_count = len(text.split()) if text.strip() else 0

c1, c2 = st.columns(2)
c1.metric("Characters", char_count)
c2.metric("Words", word_count)

# ==============================================================
# Emotion Detection + Prompt Builder (Ollama)
# ==============================================================

st.markdown("---")

generate_clicked = st.button(
    "🎨 Analyze Emotion & Generate Prompt",
    disabled=not text.strip(),
    use_container_width=True,
)

# Only hit the model when the button is pressed, or the text has
# changed since the last successful generation is *not* auto-triggered
# to avoid calling Ollama on every rerun/keystroke.
if generate_clicked and text.strip():

    with st.spinner("Analyzing emotion and building prompt..."):
        raw_response = generate_prompt(text)
        st.session_state.result = parse_response(raw_response)
        st.session_state.last_generated_text = text

result = st.session_state.result

if result is not None:

    render_summary(result)
    render_emotions(result)
    render_prompt(result["prompt"])
    render_download(result["prompt"])
    render_debug(result)

    if st.session_state.last_generated_text != text:
        st.caption(
            "⚠️ Text has changed since this analysis was generated. "
            "Click the button above to re-analyze."
        )

else:
    st.info("Enter some text (or record audio) and click the button to generate an emotion-driven image prompt.")

# ==============================================================
# IMAGE (final artwork)
# ==============================================================

st.markdown("""
<div class="section-card">
<div class="section-title">🖼️ Final Artwork</div>
<div class="section-subtitle">
Run the generated prompt through Stable Diffusion (locally) and upload the
result here
</div>
</div>
""", unsafe_allow_html=True)

uploaded_img = st.file_uploader(
    "Upload",
    type=["png", "jpg", "jpeg", "webp", "bmp", "gif"],
    label_visibility="collapsed",
)

if uploaded_img:

    st.image(
        uploaded_img,
        caption=uploaded_img.name,
        use_container_width=True,
    )

else:

    st.markdown("""
    <div class="img-placeholder">
    🖼️
    <br><br>
    No image uploaded.
    </div>
    """, unsafe_allow_html=True)
