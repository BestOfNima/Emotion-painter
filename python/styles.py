import streamlit as st


def inject_css():

    st.markdown("""
<style>

/* ==============================
   Theme
============================== */

:root{

    --primary:#6366F1;
    --secondary:#8B5CF6;

    --success:#22C55E;
    --warning:#FACC15;
    --danger:#EF4444;

    --card:#FFFFFF;
    --background:#F6F8FC;

    --text:#1E293B;
    --muted:#64748B;

}


/* ==============================
Background
============================== */

.stApp{

    background:var(--background);

}


/* ==============================
Titles
============================== */

h1,h2,h3{

    color:var(--text);

    font-weight:700;

}


/* ==============================
Section Card
============================== */

.section-card{

    background:white;

    border-radius:18px;

    padding:22px;

    margin-bottom:20px;

    border:1px solid #ECECEC;

    box-shadow:

        0 8px 24px rgba(0,0,0,.05);

}


/* ==============================
Section Title
============================== */

.section-title{

    font-size:28px;

    font-weight:700;

    margin-bottom:8px;

}


/* ==============================
Subtitle
============================== */

.section-subtitle{

    color:#64748B;

    font-size:15px;

}


/* ==============================
Prompt Box
============================== */

.stTextArea textarea{

    border-radius:16px !important;

    border:1px solid #E2E8F0 !important;

    font-size:15px;

}


/* ==============================
Metrics
============================== */

[data-testid="stMetric"]{

    background:white;

    padding:12px;

    border-radius:16px;

    border:1px solid #ECECEC;

}


/* ==============================
Buttons
============================== */

.stButton>button{

    border-radius:12px;

    border:none;

    background:#6366F1;

    color:white;

    font-weight:600;

    transition:.25s;

}

.stButton>button:hover{

    background:#4F46E5;

    transform:translateY(-2px);

}


/* ==============================
Download Button
============================== */

.stDownloadButton button{

    border-radius:12px;

    background:#22C55E;

    color:white;

}


/* ==============================
Progress
============================== */

.stProgress>div>div{

    background:#6366F1;

}


/* ==============================
Expander
============================== */

.streamlit-expanderHeader{

    font-weight:600;

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

    background:white;

    border:2px dashed #CBD5E1;

    border-radius:18px;

    padding:70px;

    text-align:center;

    color:#94A3B8;

    font-size:18px;

}


/* ==============================
Cards Hover
============================== */

.section-card:hover{

    transform:translateY(-2px);

    transition:.25s;

}


/* ==============================
Scrollbar
============================== */

::-webkit-scrollbar{

    width:8px;

}

::-webkit-scrollbar-thumb{

    background:#CBD5E1;

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

    border:2px solid white;

    box-shadow:0 3px 10px rgba(0,0,0,.15);

}


/* ==============================
JSON Viewer
============================== */

[data-testid="stJson"]{

    border-radius:16px;

}

</style>
""", unsafe_allow_html=True)