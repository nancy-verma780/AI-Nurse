import streamlit as st

import streamlit as st

st.set_page_config(
    page_title="Good Dr.",     # Title shown in browser tab
    page_icon="🩺",              # You can use an emoji, image path, or URL
    layout="wide"
)

import streamlit as st
st.set_page_config(layout="wide")
st.title("SMART DIAGNOSTICS")

col1, col2 = st.columns([2, 1])
with col1:
    st.header("Welcome to Robo Nurse: A symptom checker")
    st.write("Our AI-Powered Symptom Checker Helps You Identify Potential Causes For Your Symptoms. Simply Select Your Symptoms, And Our System Will Provide Possible Diagnoses.")
#with col2:
    #st.header("Sidebar Helpers")
    #st.image("https://media.vexels.com/media/users/3/228519/isolated/preview/cute-robot-character.png")
st.header("Robot Nurse 👨🏻‍⚕️")
st.subheader("FIND POTENTIAL CAUSES FOR YOUR SYMPTOM WITH OUR AI-POWERED TOOL")





st.markdown(
    """
    <style>
      .stApp { font-family: 'Calibri', sans-serif; }
      .stButton>button { background-color: #0d6efd; color: white; border: none; padding: 0.6em; }
      .stApp h1, .stApp h2 { color: #0a2d5f; }
    </style>
    """, unsafe_allow_html=True
)


import streamlit as st

# Override background color with light blue
st.markdown(
    """
    <style>
    .stApp, [data-testid="stAppViewContainer"] {
        background-color: #fOf8ff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#st.title(" Light Blue Background Example")
#st.write("Your app now has a soothing pale blue background!")



import streamlit as st

# Apply custom CSS styling
st.markdown(
    """
    <style>
    /* Make all headers (title, header, subheader) black */
    .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6 {
        color: #000000 !important;
    }
    /* Style all normal text (body, paragraphs, widget labels) as dark blue */
    .stApp p, .stApp div, .stApp span[data-baseweb="typography"], .stApp label {
        color: #00008B !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Your actual app content
#st.title("🎨 Header in Black, Body in Dark Blue")
#st.header("This is a header (black)")
#st.subheader("This is a subheader (black)")
#st.write("This is body text, which will appear in dark blue.")




# app.py
import streamlit as st

st.title("🥼 AI Doctor")

# Display AI doctor image
st.image(
    "https://images.openai.com/thumbnails/url/RTM02Hicu1mSUVJSUGylr5-al1xUWVCSmqJbkpRnoJdeXJJYkpmsl5yfq5-Zm5ieWmxfaAuUsXL0S7F0Tw4uDc8P8TQucfTLLXH2Kk7xMS9OKws3DU3KrqgK8Qjzcc0qLyvMMMopiQrPLfUOMskPznMN8TcvNHDSdVQrBgA-iypy",
    caption="AI Doctor",
    width=400
)
import streamlit as st

# Inject CSS to position a header at the top-left
st.markdown(
    """
    <style>
    .top-left-text {
        position: fixed;
        top: 10px;
        left: 10px;
        font-size: 24px;
        font-weight: bold;
        color: #00008B;
        z-index: 1000;
    }
    </style>
    <div class="top-left-text">🩺 Good Dr.</div>
    """,
    unsafe_allow_html=True
)

# Add some content below so the page scrolls normally
st.write("\n" * 5)
st.title("Welcome!")
#st.write("This is the main content of your page.")


import streamlit as st
import streamlit.components.v1 as components

# 1. Setup page and logo
st.set_page_config(page_title=" Good Dr.", layout="wide")
st.markdown(
    """
    <style>
      .stApp { background: linear-gradient(135deg, #e0f7fa, #fff); font-family: 'Segoe UI', sans-serif; }
      .stApp h1, .stApp h2 { color: #0a2d5f; }
      .stApp p { color: #213f7d; }
      .top-nav { position: fixed; top: 0; right: 0; padding: 10px; z-index: 1000; }
      .top-nav a { margin-left: 10px; text-decoration: none; color: #0d6efd; font-weight: bold; }
    </style>
    <div class="top-nav">
      <a href="#home">Home</a> | <a href="#about">About</a>
    </div>
    """,
    unsafe_allow_html=True
)
#st.markdown("<img src='https://.../robot_logo.png' width='48'>", unsafe_allow_html=True)

# 2. Main content
#st.title("DESCRIPION")
#st.write("Engaging description here...")

# 3. Columns for layout
#col1, col2 = st.columns([2,1])
#with col1:
    #st.header("Main Section")
    #st.write("Your main features go here.")
#with col2:
    #st.header("Sidebar")
    #st.image("https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif", width=200)

#st.markdown("<a href='#' style='background:#0d6efd;color:white;padding:10px 20px;border-radius:5px;'>Get Started</a>", unsafe_allow_html=True)


# app.py
import streamlit as st

st.title("🤖 Meet Your Cute 3D Robot")

# Use a nice animated robot (GIF) from Pixabay or Giphy
robot_gif_url = "https://media.giphy.com/media/L3SResearchCenter-robot-eldris-l3s-qUEkcv8EGkRUV4Ufl0/giphy.gif"

st.image(robot_gif_url, caption="Hello there!", width=300)


# app.py
import streamlit as st
import streamlit.components.v1 as components

# 🚀 Customize your greeting text here
greeting = "Hello! I'm chatbot, a disease identifier AI How can I assit you today?"

# Display greeting
#st.title("🤖 Auto‑Speaking Robot Assistant")
st.write(greeting)

# Inject JS to speak on page load without any user interaction or Python install
components.html(f"""
  <script>
    const msg = new SpeechSynthesisUtterance("{greeting}");
    msg.lang = "en-US";
    window.onload = () => speechSynthesis.speak(msg);
  </script>
""", height=0)


# app.py
import streamlit as st

# Initialize navigation state
if "page" not in st.session_state:
    st.session_state.page = "start"

# Diagnosis logic
def diagnose(symptoms_input):
    db = {
        "Common Cold": ["cough", "sore throat", "runny nose", "sneezing"],
        "Influenza": ["fever", "chills", "muscle aches", "fatigue", "cough"],
        "Asthma": ["wheezing", "shortness of breath", "chest tightness", "cough", "fatigue"],
        "Migraine": ["headache", "nausea", "sensitivity to light", "sensitivity to sound", "throbbing"],
        "Allergy": ["sneezing", "itchy eyes", "runny nose", "rash"],
        "Diabetes": ["increased thirst", "frequent urination", "fatigue", "blurred vision", "slow healing of wounds"],
        "Diarrhea": ["loose stools", "abdominal cramps", "bloating", "nausea"],
        "Food Poisoning": ["nausea", "diarrhea", "abdominal cramps", "fever"],
        # ... add more as needed ...
    }
    symptoms = [s.strip().lower() for s in symptoms_input.split(",") if s.strip()]
    scores = {d: len(set(symptoms) & set(keywords)) for d, keywords in db.items()}
    best = max(scores, key=scores.get)
    return f"You might have **{best}**" if scores[best] > 0 else "Please consult a doctor."

# View: Start page with 'Get Started'
def show_start():
    st.title("🩺 AI Symptom-Based Disease Identifier 📋")
    #st.image("https://static.vecteezy.com/system/resources/previews/003/961/164/original/flat-cute-cartoon-robot-illustration-transparent-background.png", width=200)
    st.write("Welcome! Click below to check your symptoms.")
    if st.button("Get Started"):
        st.session_state.page = "diagnose"

# View: Diagnose page
def show_diagnose():
    st.title("🩺 Enter Your Symptoms")
    st.write("Type symptoms separated by commas (e.g., cough, fever, fatigue).")
    symptoms = st.text_input("Your symptoms here...")
    if st.button("Diagnose"):
        if symptoms.strip():
            st.success(diagnose(symptoms))
        else:
            st.warning("Please enter symptoms before diagnosing.")
    if st.button("← Back to Home"):
        st.session_state.page = "start"

# Router logic
if st.session_state.page == "start":
    show_start()
elif st.session_state.page == "diagnose":
    show_diagnose()