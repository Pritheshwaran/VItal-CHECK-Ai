import streamlit as st
from streamlit_lottie import st_lottie
import requests
import json

def load_lottie_file(filepath: str):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Error loading animation: {e}")
        return None

def apply_custom_styling():
    st.markdown("""
    <style>
    body {
        font-family: 'Poppins', sans-serif;
        color: #2c3e50;
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    .main .block-container {
        padding: 3rem;
        max-width: 1000px;
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 20px;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
    }
    .stButton > button {
        background: linear-gradient(45deg, #3498db, #2980b9);
        color: white;
        font-weight: 600;
        border-radius: 25px;
        padding: 0.75rem 2rem;
    }
    .tooltip {
        position: relative;
        display: inline-block;
        cursor: help;
    }
    .tooltip .tooltiptext {
        visibility: hidden;
        width: 200px;
        background-color: #34495e;
        color: #fff;
        text-align: center;
        border-radius: 6px;
        padding: 10px;
        position: absolute;
        z-index: 1;
        bottom: 125%;
        left: 50%;
        margin-left: -100px;
        opacity: 0;
        transition: opacity 0.3s;
    }
    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 1;
    }
    </style>
    """, unsafe_allow_html=True)

def apply_result_styling():
    st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #e8f6f3 0%, #d1f2eb 100%);
        color: #1b5e20;
    }
    .main .block-container {
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

def create_footer():
    st.markdown("""
    <div style="text-align: center; padding: 10px; font-size: 0.8rem;">
        © 2024 VitalCheck. For educational purposes only.
    </div>
    """, unsafe_allow_html=True)

def display_lottie_animation():
    animation_path = "Animation - 1738830415214.json"
    lottie_json = load_lottie_file(animation_path)
    if lottie_json:
        st_lottie(lottie_json, speed=1, height=250, key="medical")
    else:
        st.warning("Unable to load animation. Please check the file.")

def create_info_card(title, content):
    st.markdown(f"""
    <div style="background-color: #f8f9fa; border-radius: 10px; padding: 20px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);">
        <h3 style="color: #3498db;">{title}</h3>
        <p>{content}</p>
    </div>
    """, unsafe_allow_html=True)

def create_tooltip(text, tooltip_text):
    return f"""
    <div class="tooltip">
        {text}
        <span class="tooltiptext">{tooltip_text}</span>
    </div>
    """

def main():
    st.title("Medical AI Diagnosis")
    apply_custom_styling()
    display_lottie_animation()
    
    if st.button("Run Analysis"):
        st.write("Analyzing patient data...")
        st.spinner()
        st.success("Analysis Complete!")
        apply_result_styling()
        create_info_card("Diagnosis Result", "The AI suggests a follow-up with a specialist.")
    
    create_footer()

if __name__ == "__main__":
    main()
