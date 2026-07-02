import streamlit as st

# ---------------------------------------------------------
# Color Mapping
# ---------------------------------------------------------

COLOR_MAP = {
    "Red": "#EF4444",
    "Dark Red": "#991B1B",
    "Orange": "#F97316",
    "Yellow": "#FACC15",
    "Green": "#22C55E",
    "Dark Green": "#166534",
    "Blue": "#3B82F6",
    "Dark Blue": "#1E3A8A",
    "Purple": "#A855F7",
    "Pink": "#EC4899",
    "Black": "#111827",
    "White": "#F9FAFB",
    "Gray": "#9CA3AF",
    "Brown": "#8B5A2B",
}


# ---------------------------------------------------------
# Emotion Emoji
# ---------------------------------------------------------

EMOJI = {
    "Happyness": "😊",
    "Sadness": "😢",
    "Anger": "😡",
    "Fear": "😨",
    "Calm": "😌",
}


# ---------------------------------------------------------
# Emotion Color
# ---------------------------------------------------------

EMOTION_COLOR = {
    "Happyness": "#FACC15",
    "Sadness": "#3B82F6",
    "Anger": "#EF4444",
    "Fear": "#8B5CF6",
    "Calm": "#22C55E",
}


# ---------------------------------------------------------
# Badge
# ---------------------------------------------------------

def emotion_badge(emotion: str):

    color = EMOTION_COLOR.get(emotion, "#64748B")
    emoji = EMOJI.get(emotion, "🎭")

    st.markdown(
        f"""
<div style="
background:{color};
padding:12px;
border-radius:12px;
color:white;
font-weight:700;
font-size:18px;
text-align:center;
">

{emoji} {emotion}

</div>
""",
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------
# Color Palette
# ---------------------------------------------------------

def color_palette(colors: list):

    if not colors:
        return

    html = '<div style="display:flex;gap:18px;flex-wrap:wrap;">'

    for color in colors:

        hex_color = COLOR_MAP.get(color, "#888888")

        html += f"""
<div style="text-align:center">

<div style="
width:60px;
height:60px;
border-radius:12px;
background:{hex_color};
border:2px solid #DDD;
margin:auto;
"></div>

<div style="
margin-top:8px;
font-size:14px;
font-weight:600;
">
{color}
</div>

</div>
"""

    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)