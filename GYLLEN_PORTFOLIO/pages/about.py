import streamlit as st

st.set_page_config(page_title="Gyllen G. Grezola - Home", page_icon="🏠", layout="wide")

st.markdown("""
<style>
/* Light Background for whole page */
.stApp {
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

/* Main Header */
.main-header {
    background: linear-gradient(135deg, #ff6b6b 0%, #4ecdc4 100%);
    padding: 3rem;
    border-radius: 20px;
    margin-bottom: 2rem;
    box-shadow: 0 15px 35px rgba(0,0,0,0.2);
    text-align: center;
    color: white;
}

/* Metric Cards */
.metric-card {
    background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
    padding: 2rem;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    color: #333;
}

/* Content Cards */
.content-card {
    background: rgba(255,255,255,0.9);
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.3);
}

/* Navigation Buttons */
.nav-button {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    padding: 1rem;
    border-radius: 12px;
    font-size: 1.1rem;
    font-weight: bold;
    transition: all 0.3s ease;
}
.nav-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
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

# Personal Info - Now in Light Card
st.markdown("""
<div class="content-card">
    <h2 style='text-align: center;'>👋 Welcome to My Portfolio!</h2>
    <div style='text-align: center; font-size: 1.3rem; color: #333;'>
        <p><strong>Gyllen G. Grezola</strong></p>
        <p><strong>🎓 3rd Year BSCS 3B</strong> - <strong>DEBESMSCAT</strong></p>
        <p>📍 Amoroy, Aroroy, Masbate</p>
        <p>📧 <a href='mailto:gyllengrezola4@gmail.com' style='color: #ff6b6b;'>gyllengrezola4@gmail.com</a></p>
        <p>📱 <strong>0927-223-6583</strong></p>
        <p style='color: #666; font-style: italic;'>Passionate about coding and building amazing applications!</p>
    </div>
</div>
""", unsafe_allow_html=True)

# Quick Navigation Buttons (Enhanced)
st.markdown("""
<div class="content-card">
    <h3 style='text-align: center;'>🚀 Quick Navigation</h3>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    if st.button("👨‍🎓 About Me", key="about_btn", use_container_width=True, help="Learn more about me"):
        st.switch_page("About.py")
with col2:
    if st.button("📞 Contact", key="contact_btn", use_container_width=True, help="Get in touch"):
        st.switch_page("Contact.py")

st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='
    text-align: center; 
    padding: 2rem; 
    color: #555; 
    background: rgba(255,255,255,0.8);
    border-radius: 15px;
    margin-top: 2rem;
'>
    <p style='margin: 0; font-size: 1.1rem;'>© 2025 Gyllen G. Grezola | BSCS 3B | DEBESMSCAT</p>
    <p style='margin: 0.5rem 0 0 0; color: #777;'>Made with ❤️ using Streamlit</p>
</div>
""", unsafe_allow_html=True)