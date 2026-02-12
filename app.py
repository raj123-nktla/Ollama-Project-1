import streamlit as st
import requests

st.set_page_config(page_title="Cold Outreach Generator", layout="wide")

st.title("🧊 Cold Outreach Generator (Offline AI)")

profile_text = st.text_area(
    "Paste LinkedIn Profile Text:",
    height=200,
    placeholder="Paste LinkedIn profile text here..."
)

if st.button("Generate Outreach"):
    if profile_text.strip() == "":
        st.warning("Please enter profile text.")
    else:
        with st.spinner("Generating personalized outreach..."):
            response = requests.post(
                "http://127.0.0.1:8000/generate",
                json={"profile_text": profile_text}
            )

            data = response.json()

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("📧 Cold Email")
                st.write(data["email"])

            with col2:
                st.subheader("💬 LinkedIn DM")
                st.write(data["linkedin_dm"])
