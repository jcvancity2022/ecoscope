import streamlit as st
from models.recommender import generate_recommendations

st.set_page_config(
    page_title="EcoScope – Climate Action Recommender",
    page_icon="🌍",
    layout="centered"
)

st.title("🌿 EcoScope: Your Personalized Climate Action Guide")
st.markdown("""
Welcome to **EcoScope**, a smart tool that gives you personalized, local tips to fight climate change.

Answer a few simple questions and get suggestions that fit your life 🌎💡
""")

with st.form("climate_form"):
    location = st.text_input("📍 Where do you live? (City or postal code)", help="Used to give local suggestions.")
    home_type = st.selectbox("🏠 What type of home do you live in?", ["Apartment", "Detached house", "Townhouse"])
    transport = st.selectbox("🚗 Your main form of transportation:", ["Car", "Public Transit", "Bicycle", "Walk"])
    diet = st.selectbox("🍽️ Your usual diet:", ["Meat-heavy", "Balanced", "Vegetarian", "Vegan"])
    submitted = st.form_submit_button("🔍 Get My Climate Action Tips")

if submitted:
    tips = generate_recommendations(location, home_type, transport, diet)
    st.success("✅ Based on your profile, here are your top tips:")
    for tip in tips:
        st.markdown(f"🔸 {tip}")
