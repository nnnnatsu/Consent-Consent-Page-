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

# Define the scoring
scoring = {
    "COVID-19": [("Dry cough", 2), ("Severe sore throat", 2), ("Severe headache", 2), ("Severe muscle pain", 2), ("Severe chills", 2), ("Mild diarrhea", 2), ("Severe diarrhea", 2), ("Mild loss", 2), ("Severe loss", 2)],
    "Pneumonia": [("Cough with phlegm", 2), ("Severe shortness of breath", 2), ("Severe difficulty", 2), ("Severe chills", 2)],
    "Bronchitis": [("Cough with phlegm", 2), ("Severe shortness of breath", 2), ("Mild sore throat", 2)]
}

# Streamlit app
st.title("Disease Risk Assessment")

st.markdown("""
<p>Welcome to the Disease Risk Assessment tool. Answer the following questions to assess your risk for COVID-19, Pneumonia, and Bronchitis. Click on the "Submit" button to see your results.</p>
""", unsafe_allow_html=True)

responses = []

for i, (question, choices) in enumerate(questions):
    response = st.selectbox(question, choices, key=i, index=0)
    responses.append(response)

if st.button("Submit"):
    # Calculate the scores
    scores = {"COVID-19": 0, "Pneumonia": 0, "Bronchitis": 0}

    for disease, conditions in scoring.items():
        for condition, score in conditions:
            if condition in responses:
                scores[disease] += score

    # Display the results
    st.markdown("<h2>Assessment Results</h2>", unsafe_allow_html=True)
    
    for disease, score in scores.items():
        st.markdown(f"<h4>{disease} risk score: {score}</h4>", unsafe_allow_html=True)

    total_score = sum(scores.values())
    if total_score <= 4:
        st.markdown("<h3>Low risk for COVID-19, Pneumonia, or Bronchitis (might be just a cold or irritation).</h3>", unsafe_allow_html=True)
    elif 5 <= total_score <= 9:
        st.markdown("<h3>Moderate risk for COVID-19, Pneumonia, or Bronchitis.</h3>", unsafe_allow_html=True)
    else:
        st.markdown("<h3>High risk for COVID-19, Pneumonia, or Bronchitis.</h3>", unsafe_allow_html=True)

    if total_score >= 5:
        st.markdown("<h4>Please consider consulting a healthcare provider for further evaluation.</h4>", unsafe_allow_html=True)
