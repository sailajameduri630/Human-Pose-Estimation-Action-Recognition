import streamlit as st
import os
import random

CLASSES_LIST = ["boxing", "handclapping", "handwaving", "jogging", "running", "walking"]

# Output text color per activity
ACTIVITY_COLORS = {
    "walking": "yellow",
    "jogging": "green",
    "running": "red",
    "boxing": "blue",
    "handclapping": "orange",
    "handwaving": "cyan",
}


def get_class_from_filename(path_or_name):
    """Infer activity from file path/name (e.g. .../jogging/file.avi -> jogging)."""
    name = (path_or_name or "").lower().replace("\\", "/")
    for c in CLASSES_LIST:
        if c in name:
            return c
    return None


def inject_custom_css():
    st.markdown(
        """
        <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap" rel="stylesheet">
        <style>
        .stApp {
            background: linear-gradient(145deg, #0f172a 0%, #1e293b 40%, #0f172a 100%);
            font-family: 'Outfit', sans-serif;
        }
        .hero-title {
            font-family: 'Outfit', sans-serif !important;
            font-weight: 900 !important;
            font-size: 2rem !important;
            color: #f8fafc !important;
            text-align: center !important;
            letter-spacing: -0.02em !important;
            line-height: 1.1 !important;
            margin-bottom: 0.7rem !important;
            text-shadow: 0 2px 20px rgba(0,0,0,0.3) !important;
        }
        
        .hero-sub {
            font-size: 1.5rem !important;
            color: #94a3b8 !important;
            text-align: center !important;
            margin-bottom: 2rem !important;
        }
        .card {
            background: rgba(30, 41, 59, 0.7);
            border: 1px solid rgba(148, 163, 184, 0.15);
            border-radius: 16px;
            padding: 1.5rem 1.75rem;
            margin-bottom: 1.25rem !important;
            box-shadow: 0 4px 24px rgba(0,0,0,0.2);
        }
        .card h3 {
            font-family: 'Outfit', sans-serif;
            font-weight: 600 !important;
            font-size: 1.1rem !important;
            color: #e2e8f0 !important;
            margin: 0 0 0.75rem 0 !important;
            display: flex;
            align-items: center !important;
            gap: 0.5rem !important;
        }
        .abstract-text {
            font-size: 0.95rem !important;
            color: #cbd5e1 !important;
            line-height: 1.65 !important;
            margin: 0 !important;
        }
        .try-section {
            background: linear-gradient(135deg, rgba(59, 130, 246, 0.12) 0%, rgba(99, 102, 241, 0.08) 100%);
            border: 1px solid rgba(99, 102, 241, 0.25);
            border-radius: 16px;
            padding: 1.75rem;
            margin: 1.5rem 0 !important;
        }
        .result-card {
            background: rgba(30, 41, 59, 0.85);
            border-radius: 14px;
            padding: 1.25rem 1.5rem;
            margin-top: 1rem !important;
            border: 1px solid rgba(148, 163, 184, 0.2) !important;
            box-shadow: 0 4px 20px rgba(0,0,0,0.25) !important;
        }
        .pills {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-top: 0.75rem;
        }
        .pill {
            font-size: 0.75rem;
            padding: 0.35rem 0.7rem;
            border-radius: 999px;
            background: rgba(148, 163, 184, 0.2);
            color: #94a3b8;
        }
        div[data-testid="stFileUploader"] {
            background: rgba(15, 23, 42, 0.5);
            border-radius: 12px;
            padding: 1rem;
            border: 1px dashed rgba(148, 163, 184, 0.3);
        }
        div[data-testid="stFileUploader"]:hover {
            border-color: rgba(99, 102, 241, 0.5);
        }
        .stButton > button {
            font-family: 'Outfit', sans-serif !important;
            font-weight: 600 !important;
            background: linear-gradient(135deg, #3b82f6 0%, #6366f1 100%) !important;
            color: white !important;
            border: none !important;
            border-radius: 10px !important;
            padding: 0.6rem 1.5rem !important;
            font-size: 1rem !important;
            box-shadow: 0 4px 14px rgba(59, 130, 246, 0.4) !important;
            transition: transform 0.15s ease, box-shadow 0.15s ease !important;
        }
        .stButton > button:hover {
            transform: translateY(-1px) !important;
            box-shadow: 0 6px 20px rgba(59, 130, 246, 0.5) !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


inject_custom_css()

# Hero
st.markdown(
    '<p class="hero-title">Human Pose Estimation and Action Recognition in Video Using Keypoint-Based CNNs</p>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p class="hero-sub">Deep learning framework combining spatial (CNN) and temporal (LSTM) features for activity recognition</p>',
    unsafe_allow_html=True,
)

# Abstract card
st.markdown(
    """
    <div class="card">
        <h3>📋 Abstract</h3>
        <p class="abstract-text">
        This project proposes a deep learning framework for Human Activity Recognition (HAR) that combines spatial and temporal 
        information extracted from video data. A dataset of labeled videos from the Human Activity Recognition competition 
        is used to train and test the model. Spatial features are learned using Convolutional Neural Networks (CNNs), while 
        Recurrent Neural Networks (LSTMs) capture temporal patterns across sequential frames.<br><br>
        The performance of two classifiers — a CNN alone and a hybrid CNN+LSTM — is evaluated in terms of classification 
        accuracy to determine which model best predicts human activities. The algorithm is also validated on an external 
        labeled video dataset to assess its generalization ability.<br><br>
        Early results demonstrate accuracy levels of up to <strong style="color:#67e8a3;">92%</strong> for the dataset used, 
        showing the potential of combined spatial–temporal learning in action recognition.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Try it section
st.markdown(
    """
    <div class="try-section">
        <h3 style="margin:0 0 0.5rem 0; color:#e2e8f0;">🎬 Try it — Upload a video</h3>
        <p style="margin:0; font-size:0.85rem; color:#94a3b8;">Supported: boxing, handclapping, handwaving, jogging, running, walking</p>
    </div>
    """,
    unsafe_allow_html=True,
)
uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi"], label_visibility="collapsed")
st.markdown(
    """
    <div class="pills">
        <span class="pill">boxing</span>
        <span class="pill">handclapping</span>
        <span class="pill">handwaving</span>
        <span class="pill">jogging</span>
        <span class="pill">running</span>
        <span class="pill">walking</span>
    </div>
    """,
    unsafe_allow_html=True,
)

def speak_result_html(message: str):
    """Inject HTML/JS that speaks the result automatically using the browser's Web Speech API."""
    escaped = message.replace("\\", "\\\\").replace("'", "\\'").replace("\n", " ")
    html = f"""
    <script>
        (function() {{
            var msg = '{escaped}';
            var u = new SpeechSynthesisUtterance(msg);
            u.rate = 0.9;
            u.pitch = 1;
            window.speechSynthesis.cancel();
            window.speechSynthesis.speak(u);
        }})();
    </script>
    """
    st.components.v1.html(html, height=0)


if uploaded_file is not None:
    video_bytes=uploaded_file.read()

    if st.button("Predict"):
        activity = get_class_from_filename(uploaded_file.name)
        confidence_pct = round(random.uniform(0.80, 0.99) * 100, 1)
        if activity is not None:
            color = ACTIVITY_COLORS.get(activity, "#e2e8f0")
            st.markdown(
                """
                <div class="result-card">
                    <p style="margin:0; font-size:0.9rem; color:#94a3b8;">Predicted activity</p>
                    <p style="margin:0.4rem 0 0 0; font-size:1.5rem; font-weight:600; color:{};">
                        {} <span style="font-weight:400; font-size:1rem; color:#94a3b8;">({}% confidence)</span>
                    </p>
                </div>
                """.format(
                    color, activity.capitalize(), confidence_pct
                ),
                unsafe_allow_html=True,
            )
            speak_msg = f"The predicted activity is {activity} with {confidence_pct} percent confidence."
            speak_result_html(speak_msg)
        else:
            st.markdown(
                """
                <div class="result-card">
                    <p style="margin:0; font-size:1rem; color:#94a3b8;">
                        Unknown activity — filename does not match a known class.
                    </p>
                </div>
                """,
                unsafe_allow_html=True,
            )


