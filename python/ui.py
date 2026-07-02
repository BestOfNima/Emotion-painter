import json

import streamlit as st

from python.palette import (
    emotion_badge,
    color_palette,
)

from python.charts import (
    emotion_progress,
    radar_chart,
    donut_chart,
)

from python.constants import (
    STYLE_ICON,
)

def render_prompt(prompt: str):

    st.subheader("🎨 Generated Prompt")

    st.text_area(
        "Prompt",
        value=prompt,
        height=220,
        disabled=True,
        label_visibility="collapsed",
    )

def render_summary(data: dict):

    st.subheader("📊 Summary")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### Dominant Emotion")

        emotion_badge(
            data["dominant_emotion"]
        )

    with col2:

        st.markdown("### Style")

        st.info(
            f"{STYLE_ICON} {data['style']}"
        )

    st.markdown("### Color Palette")

    color_palette(
        data["colors"]
    )

def render_emotions(data: dict):

    dna = data["emotion_dna"]

    emotion_progress(dna)

    c1, c2 = st.columns(2)

    with c1:

        radar_chart(dna)

    with c2:

        donut_chart(dna)

def render_debug(data: dict):

    with st.expander("JSON Output"):

        st.json(data)

def render_download(prompt: str):

    st.download_button(

        "⬇ Download Prompt",

        prompt,

        file_name="prompt.txt",

        mime="text/plain",

    )