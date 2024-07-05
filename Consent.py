import streamlit as st

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

responses = []

for i, (question, choices) in enumerate(questions):
    response = st.selectbox(question, choices, key=i)
    responses.append(response)

# Calculate the scores
scores = {"COVID-19": 0, "Pneumonia": 0, "Bronchitis": 0}

for disease, conditions in scoring.items():
    for condition, score in conditions:
        if condition in responses:
            scores[disease] += score

# Display the results
st.header("Assessment Results")
for disease, score in scores.items():
    st.write(f"{disease} risk score: {score}")

total_score = sum(scores.values())
if total_score <= 4:
    st.write("Low risk for COVID-19, Pneumonia, or Bronchitis (might be just a cold or irritation).")
elif 5 <= total_score <= 9:
    st.write("Moderate risk for COVID-19, Pneumonia, or Bronchitis.")
else:
    st.write("High risk for COVID-19, Pneumonia, or Bronchitis.")

if total_score >= 5:
    st.write("Please consider consulting a healthcare provider for further evaluation.")
