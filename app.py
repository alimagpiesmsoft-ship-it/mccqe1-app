import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="MCCQE1 Pediatric Quiz AI", layout="centered")

st.title("🩺 MCCQE1 AI Exam Generator")
st.subheader("Pediatrics Module")

st.sidebar.title("Configuration")
api_key = st.sidebar.text_input("Enter your Gemini API Key:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # استخدام النسخة الأكثر توافقاً مع جميع المناطق والإصدارات
        model = genai.GenerativeModel('gemini-1.0-pro')

        topic = st.selectbox("Select a Pediatric Topic:", 
                             ["Neonatology", "Respiratory", "GI", "Emergency", "Cardiology", "Growth & Development"])

        if st.button("Generate New Question"):
            prompt = f"Act as an MCCQE1 examiner. Generate a high-yield clinical vignette question about Pediatric {topic}. Include 4 options (A, B, C, D), the correct answer, and a detailed rationale based on Canadian guidelines (CPS)."
            
            with st.spinner("Generating your question..."):
                response = model.generate_content(prompt)
                st.session_state.question = response.text

        if 'question' in st.session_state:
            st.markdown("---")
            st.markdown(st.session_state.question)
            
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Please enter your Gemini API Key in the sidebar to start.")
