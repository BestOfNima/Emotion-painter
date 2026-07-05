import streamlit as st


def inject_css():

    st.markdown("""
<style>

p{font-size: 25px !important;}

/* ==============================
   Theme — Light (default)
============================== */

:root{

    --primary:#6366F1;
    --secondary:#8B5CF6;

    --success:#22C55E;
    --warning:#FACC15;
    --danger:#EF4444;

    --card:#FFFFFF;
    --card-border:#ECECEC;
    --background:#F6F8FC;

    --text:#1E293B;
    --muted:#64748B;

    --input-bg:#FFFFFF;
    --input-border:#E2E8F0;

    --placeholder-border:#CBD5E1;
    --placeholder-text:#94A3B8;

    --scrollbar:#CBD5E1;

    --shadow: rgba(0,0,0,.05);
    --shadow-strong: rgba(0,0,0,.10);

}


/* ==============================
   Theme — Dark (auto, OS/browser)
============================== */

@media (prefers-color-scheme: dark){

    :root{

        --card:#1A1D27;
        --card-border:#2D3148;
        --background:#0F1117;

        --text:#F1F5F9;
        --muted:#94A3B8;

        --input-bg:#111827;
        --input-border:#374151;

        --placeholder-border:#374151;
        --placeholder-text:#6B7280;

        --scrollbar:#374151;

        --shadow: rgba(0,0,0,.35);
        --shadow-strong: rgba(0,0,0,.55);

    }

}


/* ==============================
Background
============================== */

.stApp{

    background:var(--background);
    color:var(--text);

}


/* ==============================
Titles
============================== */

h1,h2,h3{

    color:var(--text);

    font-weight:700;

}

p, span, label, .stMarkdown{

    color:var(--text);

}


/* ==============================
Section Card
============================== */

.section-card{

    background:var(--card);

    border-radius:18px;

    padding:22px;

    margin-bottom:20px;

    border:1px solid var(--card-border);

    box-shadow:

        0 8px 24px var(--shadow);

}


/* ==============================
Section Title
============================== */

.section-title{

    font-size:28px;

    font-weight:700;

    margin-bottom:8px;

    color:var(--text);

}


/* ==============================
Subtitle
============================== */

.section-subtitle{

    color:var(--muted);

    font-size:15px;

}


/* ==============================
Prompt Box
============================== */

.stTextArea textarea{

    background:var(--input-bg) !important;

    border-radius:16px !important;

    border:1px solid var(--input-border) !important;

    color:var(--text) !important;

    font-size:15px;

}


/* ==============================
Metrics
============================== */

[data-testid="stMetric"]{

    background:var(--card);

    padding:12px;

    border-radius:16px;

    border:1px solid var(--card-border);

}

[data-testid="stMetricValue"],
[data-testid="stMetricLabel"]{

    color:var(--text);

}


/* ==============================
Buttons
============================== */

.stButton>button{

    border-radius:12px;

    border:none;

    background:var(--primary);

    color:white;

    font-weight:600;

    transition:.25s;

}

.stButton>button:hover{

    background:var(--secondary);

    transform:translateY(-2px);

}


/* ==============================
Download Button
============================== */

.stDownloadButton button{

    border-radius:12px;

    background:var(--success);

    color:white;

}


/* ==============================
Progress
============================== */

.stProgress>div>div{

    background:var(--primary);

}


/* ==============================
Expander
============================== */

.streamlit-expanderHeader{

    font-weight:600;

    color:var(--text);

    background:var(--card);

}

.streamlit-expanderContent{

    background:var(--card);

    color:var(--text);

}


/* ==============================
Audio
============================== */

audio{

    width:100%;

}


/* ==============================
Image Placeholder
============================== */

.img-placeholder{

    background:var(--card);

    border:2px dashed var(--placeholder-border);

    border-radius:18px;

    padding:70px;

    text-align:center;

    color:var(--placeholder-text);

    font-size:18px;

}


/* ==============================
Cards Hover
============================== */

.section-card:hover{

    transform:translateY(-2px);

    box-shadow:0 12px 28px var(--shadow-strong);

    transition:.25s;

}


/* ==============================
Scrollbar
============================== */

::-webkit-scrollbar{

    width:8px;

}

::-webkit-scrollbar-thumb{

    background:var(--scrollbar);

    border-radius:8px;

}


/* ==============================
Emotion Badge
============================== */

.emotion-card{

    border-radius:16px;

    color:white;

    padding:18px;

    text-align:center;

    font-size:20px;

    font-weight:700;

}


/* ==============================
Color Palette
============================== */

.color-box{

    width:58px;

    height:58px;

    border-radius:12px;

    border:2px solid var(--card);

    box-shadow:0 3px 10px var(--shadow-strong);

}


/* ==============================
JSON Viewer
============================== */

[data-testid="stJson"]{

    border-radius:16px;

    background:var(--card);

}

</style>
""", unsafe_allow_html=True)