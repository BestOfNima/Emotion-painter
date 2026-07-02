import os
import uuid
from datetime import datetime

import streamlit as st

from python.app_STT import transcribe
from python.app_ollama import generate_prompt

# ───────────────────────────────────────────────────────────────
# Page config
# ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Audio · Text · Image Studio",
    page_icon="🎙️",
    layout="centered",
)

os.makedirs("audio", exist_ok=True)

# ───────────────────────────────────────────────────────────────
# Session State
# ───────────────────────────────────────────────────────────────
if "text_content" not in st.session_state:
    st.session_state.text_content = ""

if "last_audio_id" not in st.session_state:
    st.session_state.last_audio_id = None

if "current_audio_filename" not in st.session_state:
    st.session_state.current_audio_filename = None

# ───────────────────────────────────────────────────────────────
# CSS
# ───────────────────────────────────────────────────────────────
st.markdown("""
<style>

.stApp {
    background-color:#0f1117;
}

.section-card{
    background:#1a1d27;
    border:1px solid #2d3148;
    border-radius:16px;
    padding:28px 32px 24px;
    margin-bottom:24px;
}

.section-title{
    font-size:1.15rem;
    font-weight:700;
    letter-spacing:.04em;
    text-transform:uppercase;
    margin-bottom:6px;
}

.section-title.audio{
    color:#a78bfa;
}

.section-title.text{
    color:#60a5fa;
}

.section-title.image{
    color:#34d399;
}

.section-subtitle{
    color:#6b7280;
    font-size:.85rem;
    margin-bottom:18px;
}

.saved-badge{
    display:inline-flex;
    align-items:center;
    gap:6px;
    background:#14532d;
    color:#86efac;
    border-radius:8px;
    padding:6px 12px;
    font-size:.82rem;
    font-weight:600;
    margin-top:10px;
}

.img-placeholder{
    border:2px dashed #2d3148;
    border-radius:12px;
    padding:48px 24px;
    text-align:center;
    color:#4b5563;
}

label{
    color:#9ca3af !important;
}

.stTextArea textarea{
    background:#111827 !important;
    border:1px solid #374151 !important;
    border-radius:10px !important;
    color:white !important;
}

.tagline{
    color:#6b7280;
    margin-top:-10px;
    margin-bottom:28px;
}

</style>
""", unsafe_allow_html=True)

# ───────────────────────────────────────────────────────────────
# Title
# ───────────────────────────────────────────────────────────────
st.markdown("# 🎙️ Studio")
st.markdown(
    '<p class="tagline">Record · Write · Display</p>',
    unsafe_allow_html=True,
)

# ==============================================================
# AUDIO
# ==============================================================

st.markdown("""
<div class="section-card">
<div class="section-title audio">🎤 Record Audio</div>
<div class="section-subtitle">
Press the microphone button to record.
</div>
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
<div class="section-title text">✍️ Write Text</div>
<div class="section-subtitle">
Write anything or use speech-to-text.
</div>
</div>
""", unsafe_allow_html=True)

text = st.text_area(
    "Text",
    value=st.session_state.text_content,
    height=180,
    label_visibility="collapsed",
)

# ذخیره آخرین مقدار تایپ شده
st.session_state.text_content = text

char_count = len(text)
word_count = len(text.split()) if text.strip() else 0

c1, c2 = st.columns(2)

c1.metric("Characters", char_count)
c2.metric("Words", word_count)

# ==============================================================
# Prompt Generation
# ==============================================================

st.markdown("---")
st.subheader("🎨 Generated Image Prompt")

if text.strip():

    with st.spinner("Generating Prompt..."):

        prompt = generate_prompt(text)

    st.text_area(
        "Prompt",
        value=prompt,
        height=240,
        disabled=True,
    )

else:

    st.info("Enter some text to generate an image prompt.")

# ==============================================================
# IMAGE
# ==============================================================

st.markdown("""
<div class="section-card">
<div class="section-title image">🖼️ Image Display</div>
<div class="section-subtitle">
Upload an image.
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