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

_COLOR_MAP_LOWER = {k.lower(): v for k, v in COLOR_MAP.items()}


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

_EMOJI_LOWER = {k.lower(): v for k, v in EMOJI.items()}


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

_EMOTION_COLOR_LOWER = {k.lower(): v for k, v in EMOTION_COLOR.items()}


# ---------------------------------------------------------
# Badge
# ---------------------------------------------------------

def emotion_badge(emotion: str):

    key = str(emotion).strip().lower()

    color = _EMOTION_COLOR_LOWER.get(key, "#64748B")
    emoji = _EMOJI_LOWER.get(key, "🎭")

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

def color_palette(colors):

    if not colors:
        return

    # Defensive: handle a stray comma-separated string, even though
    # parser.parse_response() should already have normalized this to a list.
    if isinstance(colors, str):
        colors = [c.strip() for c in colors.split(",") if c.strip()]

    if not colors:
        return

    html = '<div style="display:flex;gap:18px;flex-wrap:wrap;">'

    for color in colors:

        hex_color = _COLOR_MAP_LOWER.get(str(color).strip().lower(), "#888888")

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
