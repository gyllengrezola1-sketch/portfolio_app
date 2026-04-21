import streamlit as st

st.set_page_config(page_title="Gyllen G. Grezola - Home", page_icon="🏠", layout="wide")

st.markdown("""
<style>
.main-header {
    background: linear-gradient(135deg, #ff6b6b 0%, #4ecdc4 100%);
    padding: 3rem;
    border-radius: 20px;
    margin-bottom: 2rem;
    box-shadow: 0 15px 35px rgba(0,0,0,0.2);
    text-align: center;
    color: white;
}
.metric-card {
    background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
    padding: 2rem;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);
}
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="main-header">
    <h1 style='margin: 0; font-size: 3rem;'>Gyllen G. Grezola</h1>
    <p style='font-size: 1.5rem; margin-top: 1rem;'>BSCS 3B Student | DEBESMSCAT</p>
</div>
""", unsafe_allow_html=True)

# Stats Cards
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="metric-card">
        <h2 style='margin: 0; font-size: 2.5rem;'>21</h2>
        <p style='margin: 0.5rem 0 0 0; font-size: 1.2rem;'>Years Old</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h2 style='margin: 0; font-size: 2.5rem;'>3B</h2>
        <p style='margin: 0.5rem 0 0 0; font-size: 1.2rem;'>BSCS Student</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <h2 style='margin: 0; font-size: 2.5rem;'>DEBESMSCAT</h2>
        <p style='margin: 0.5rem 0 0 0; font-size: 1.2rem;'>University</p>
    </div>
    """, unsafe_allow_html=True)

# Personal Info
st.markdown("## 👋 Welcome to My Portfolio!")
st.markdown("""
**Gyllen G. Grezola**  
**🎓 3rd Year BSCS 3B** - **DEBESMSCAT**  
**📍 Amoroy, Aroroy, Masbate**  
**📧 gyllengrezola4@gmail.com**  
**📱 0927-223-6583**  

Passionate about coding and building amazing applications!
""")

# Quick Navigation Buttons (ONLY About & Contact)
st.markdown("### 🚀 Quick Navigation")
col1, col2 = st.columns(2)
with col1:
    if st.button("👨‍🎓 About Me", use_container_width=True):
        st.switch_page("About.py")
with col2:
    if st.button("📞 Contact", use_container_width=True):
        st.switch_page("Contact.py")

st.markdown("---")
st.markdown("<p style='text-align: center; color: #666;'>© 2025 Gyllen G. Grezola | BSCS 3B | DEBESMSCAT</p>", unsafe_allow_html=True)