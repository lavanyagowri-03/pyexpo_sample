import streamlit as st
st.set_page_config(page_title="My Portfolio", page_icon="🌟")
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Home", "About", "Projects", "Contact"])
if menu == "Home":
    st.title("👩‍💻INNO CORES")
    st.subheader("Aspiring Full Stack Developer")
    st.write("Welcome to my Streamlit portfolio!")
elif menu == "About":
    st.header(" About Me")
    st.write("""
    - Beginner Full Stack Developer  
    - Learning Python, C, Streamlit  
    - Interested in Web & App Development  
    """)
elif menu == "Projects":
    st.header(" Projects")
    st.write("🔹 Student Navigation System")
    st.write("🔹 Water Management System")
    st.write("🔹 Emotion Detection System")
elif menu == "Contact":
    st.header(" Contact Me")
    email = st.text_input("Enter your email")
    msg = st.text_area("Your message")
    if st.button("Send"):
        st.success("Message sent successfully")