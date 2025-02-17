import streamlit as st
import google.generativeai as genai
from ui_ux import (
    apply_custom_styling, 
    create_footer, 
    display_lottie_animation, 
    create_info_card, 
    create_tooltip
)
genai.configure(api_key="YOUR API KEY")

def get_gemini_response(input_text):
    """Use Google Gemini AI for fast disease prediction."""
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"Given these symptoms: {input_text}, predict possible diseases with high accuracy. Provide a brief explanation for each prediction."
    response = model.generate_content(prompt)
    return response.text.strip()


st.set_page_config(
    page_title="VitalCheck 🩺",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed"
)

apply_custom_styling()


with st.container():
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("<h1>VitalCheck 🩺</h1>", unsafe_allow_html=True) 
        st.markdown("<h4>Your AI-Powered Medical Assistant</h4>", unsafe_allow_html=True)
    with col2:
        display_lottie_animation()

    st.markdown("<hr>", unsafe_allow_html=True)

st.markdown("<p>Answer the following questions to analyze your symptoms accurately.</p>", unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    create_info_card("How It Works", "VitalCheck uses advanced AI to analyze your symptoms and suggest possible conditions. Remember, this is not a substitute for professional medical advice.")
with col2:
    create_info_card("Privacy Note", "Your health information is important. We do not store any personal data you enter here.")


symptoms_list = [
    "Headache",
    "Fever",
    "Cough",
    "Shortness of breath",
    "Nausea",
    "Fatigue",
    "Muscle aches",
    "Sore throat"
]


user_symptoms = []

st.markdown('<div class="symptom-container">', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
for i, symptom in enumerate(symptoms_list):
    with col1 if i % 3 == 0 else col2 if i % 3 == 1 else col3:
        tooltip = create_tooltip(
            f"Do you have {symptom}?",
            f"Select 'Yes' if you're experiencing {symptom.lower()}."
        )
        st.markdown(tooltip, unsafe_allow_html=True)
        response = st.radio("", ('No', 'Yes'), key=symptom, label_visibility="collapsed")
        if response == 'Yes':
            user_symptoms.append(symptom.lower())
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
other_symptoms = st.text_input(
    "Any other symptoms you want to add?",
    placeholder="e.g., dizziness, back pain"
)
if other_symptoms:
    other_symptoms_list = [symptom.strip().lower() for symptom in other_symptoms.split(',')]
    user_symptoms.extend(other_symptoms_list)


st.markdown("<hr>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button("Analyze Symptoms"):
        if user_symptoms:
            with st.spinner("Analyzing your symptoms..."):
                symptoms_str = ', '.join(user_symptoms)
                prediction = get_gemini_response(symptoms_str)

            if prediction:
                st.markdown('<div class="prediction-container">', unsafe_allow_html=True)
                st.success("Analysis complete! Here are the results:")
                st.markdown(f"<p style='font-size:20px;'><b>Possible conditions based on your symptoms:</b></p>", unsafe_allow_html=True)
                st.info(prediction)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.warning("The prediction was inconclusive. Please refine your symptoms or consult a healthcare professional.")
        else:
            st.warning("Please select at least one symptom or add additional symptoms.")


create_footer()
