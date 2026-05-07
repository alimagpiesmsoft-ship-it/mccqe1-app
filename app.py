import streamlit as st
import google.generativeai as genai

# إعداد واجهة الموقع
st.set_page_config(page_title="MCCQE1 Pediatric Quiz AI", layout="centered")

st.title("🩺 MCCQE1 AI Exam Generator")
st.subheader("Pediatrics Module")

# إدخال الـ API Key من الشريط الجانبي
st.sidebar.title("Configuration")
api_key = st.sidebar.text_input("Enter your Gemini API Key:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # التحديث هنا: استخدام موديل flash بدلاً من pro القديم
        model = genai.GenerativeModel('gemini-1.5-flash')

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
        st.error(f"Something went wrong: {e}")
else:
    st.info("Please enter your Gemini API Key in the sidebar to start.")
