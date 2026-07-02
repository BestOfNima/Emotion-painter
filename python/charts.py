import streamlit as st
import plotly.graph_objects as go

from python.constants import (
    EMOTIONS,
    EMOTION_COLORS,
    EMOJI,
)


# -------------------------------------------------------
# Progress Bars
# -------------------------------------------------------

def emotion_progress(dna: dict):

    st.subheader("😊 Emotion Analysis")

    for emotion in EMOTIONS:

        value = dna.get(emotion.lower(), 0)

        col1, col2 = st.columns([7, 1])

        with col1:
            st.markdown(
                f"**{EMOJI[emotion]} {emotion}**"
            )
            st.progress(value / 100)

        with col2:
            st.metric("", f"{value}%")

def radar_chart(dna: dict):

    values = [
        dna.get(e.lower(), 0)
        for e in EMOTIONS
    ]

    values.append(values[0])

    labels = EMOTIONS.copy()
    labels.append(labels[0])

    fig = go.Figure()

    fig.add_trace(
        go.Scatterpolar(
            r=values,
            theta=labels,
            fill="toself",
            line=dict(width=3),
            marker=dict(size=8),
        )
    )

    fig.update_layout(
        title="Emotion Radar",
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
            )
        ),
        showlegend=False,
        height=420,
    )

    st.plotly_chart(fig, use_container_width=True)

def bar_chart(dna: dict):

    values = [
        dna.get(e.lower(), 0)
        for e in EMOTIONS
    ]

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=EMOTIONS,
            y=values,
            marker_color=[
                EMOTION_COLORS[e]
                for e in EMOTIONS
            ],
        )
    )

    fig.update_layout(
        title="Emotion Distribution",
        yaxis=dict(range=[0, 100]),
        height=420,
        showlegend=False,
    )

    st.plotly_chart(fig, use_container_width=True)

def donut_chart(dna: dict):

    values = [
        dna.get(e.lower(), 0)
        for e in EMOTIONS
    ]

    fig = go.Figure(
        go.Pie(
            labels=EMOTIONS,
            values=values,
            hole=0.65,
            marker=dict(
                colors=[
                    EMOTION_COLORS[e]
                    for e in EMOTIONS
                ]
            ),
        )
    )

    fig.update_layout(
        title="Emotion Ratio",
        height=420,
    )

    st.plotly_chart(fig, use_container_width=True)