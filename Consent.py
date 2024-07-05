import streamlit as st

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 2rem;
    }
    .reportview-container .main .block-container {
        padding: 2rem;
        border-radius: 10px;
        background-color: white;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .stButton button {
        border-radius: 5px;
        background-color: #007bff;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #0056b3;
    }
    .stSelectbox {
        padding: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Define the questions and choices
questions = [
    ("Do you have a high fever?", ["No fever", "Mild fever", "High fever over 38°C"]),
    ("What type of cough do you have?", ["No cough", "Dry cough", "Cough with phlegm"]),
    ("Do you experience shortness of breath?", ["No shortness of breath", "Mild shortness of breath", "Severe shortness of breath"]),
    ("Do you have a sore throat?", ["No sore throat", "Mild sore throat", "Severe sore throat"]),
    ("Do you experience difficulty breathing?", ["Breathing easily", "Mild difficulty", "Severe difficulty"]),
    ("Do you have a headache?", ["No headache", "Mild headache", "Severe headache"]),
    ("Do you have muscle pain?", ["No muscle pain", "Mild muscle pain", "Severe muscle pain"]),
    ("Do you experience chills?", ["No chills", "Mild chills", "Severe chills"]),
    ("Do you have diarrhea?", ["No diarrhea", "Mild diarrhea", "Severe diarrhea"]),
    ("Do you experience loss of taste or smell?", ["No loss", "Mild loss", "Severe loss"])
]

# Streamlit app
st.title("Disease Risk Assessment")

st.markdown("""
<p>Welcome to the Disease Risk Assessment tool. Answer the following questions to assess your risk for COVID-19, Pneumonia, and Bronchitis. Click on the "Next" button to proceed to the audio classification page.</p>
""", unsafe_allow_html=True)

responses = []

for i, (question, choices) in enumerate(questions):
    response = st.selectbox(question, choices, key=i, index=0)
    responses.append(response)

# Link to the second app on Hugging Face
if st.button("Next"):
    st.markdown("""
        <meta http-equiv="refresh" content="0; url=https://nnnnnnnatsu-cough4sound.hf.space" />
    """, unsafe_allow_html=True)
