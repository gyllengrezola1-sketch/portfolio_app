import streamlit as st

st.set_page_config(page_title="Contact - Gyllen", page_icon="📞", layout="wide")

st.markdown("""
<style>
/* Light Background for whole page */
.stApp {
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}

/* Contact Header */
.contact-header {
    background: linear-gradient(135deg, #4ecdc4 0%, #44a08d 100%);
    padding: 2.5rem;
    border-radius: 20px;
    margin-bottom: 2rem;
    text-align: center;
    color: white;
    box-shadow: 0 15px 35px rgba(0,0,0,0.2);
}

/* Content Cards - Semi-transparent for readability */
.contact-card {
    background: rgba(255,255,255,0.95);
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.4);
    color: #333;
}

/* Form styling */
.form-input {
    border-radius: 10px;
    border: 2px solid #e0e0e0;
}

/* Buttons */
.submit-btn {
    background: linear-gradient(135deg, #ff6b6b 0%, #4ecdc4 100%);
    color: white;
    border: none;
    padding: 0.8rem;
    border-radius: 12px;
    font-weight: bold;
}
.clear-btn {
    background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
    color: #333;
    border: none;
    padding: 0.8rem;
    border-radius: 12px;
    font-weight: bold;
}

/* Footer */
.footer-card {
    background: rgba(255,255,255,0.9);
    padding: 1.5rem;
    border-radius: 15px;
    text-align: center;
    color: #555;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="contact-header">
    <h1 style='margin: 0; font-size: 2.5rem;'>📞 Get In Touch</h1>
    <p style='font-size: 1.3rem; margin-top: 0.5rem;'>Connect with Gyllen G. Grezola</p>
</div>
""", unsafe_allow_html=True)

# Contact Info + Form
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="contact-card">
        <h3 style='color: #333; margin-bottom: 1rem;'>📱 Contact Details</h3>
        <hr style='border: 1px solid #e0e0e0;'>
        <div style='font-size: 1.1rem; line-height: 1.8;'>
            <p><strong>📧 Email:</strong></p>
            <p style='font-size: 1.2rem; color: #ff6b6b; margin: 0.5rem 0;'>
                <a href='mailto:gyllengrezola4@gmail.com' style='color: #ff6b6b; text-decoration: none;'>gyllengrezola4@gmail.com</a>
            </p>
            <p><strong>📱 Phone:</strong></p>
            <p style='font-size: 1.2rem; font-weight: bold; color: #4ecdc4; margin: 0.5rem 0;'>0927-223-6583</p>
            <p><strong>📍 Address:</strong></p>
            <p style='font-size: 1.1rem;'>Amoroy, Aroroy, Masbate</p>
            <p><strong>🏫 School:</strong></p>
            <p style='font-size: 1.1rem; font-weight: bold;'>BSCS 3B - DEBESMSCAT</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="contact-card">
        <h3 style='color: #333; margin-bottom: 1rem;'>💬 Send Message</h3>
    """, unsafe_allow_html=True)
    
    with st.form("contact_form"):
        name = st.text_input("👤 Your Name", placeholder="Enter your name")
        email = st.text_input("📧 Your Email", placeholder="your@email.com")
        subject = st.text_input("📝 Subject", placeholder="What is this about?")
        message = st.text_area("💬 Message", height=150, placeholder="Tell me more...")
        
        col1, col2 = st.columns(2)
        with col1:
            submitted = st.form_submit_button("🚀 Send Message", use_container_width=True)
        with col2:
            clear_btn = st.form_submit_button("🗑️ Clear Form", use_container_width=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    if submitted:
        if name and email and message:
            st.success("""
            ✅ **Message sent successfully!**  
            I'll reply within 24 hours! ✨
            """)
            st.balloons()
        else:
            st.error("❌ **Please fill all fields!**")
    
    if clear_btn:
        st.rerun()

# Back to Home Button
st.markdown("""
<div class="contact-card" style='text-align: center;'>
""", unsafe_allow_html=True)
if st.button("🏠 Back to Home", use_container_width=True, key="home_btn"):
    st.switch_page("Home.py")
st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer-card">
    <p style='margin: 0; font-size: 1.1rem;'>© 2025 Gyllen G. Grezola | BSCS 3B | DEBESMSCAT</p>
    <p style='margin: 0.5rem 0 0 0; color: #777; font-size: 0.95rem;'>Made with ❤️ using Streamlit</p>
</div>
""", unsafe_allow_html=True)