import streamlit as st
import streamlit.components.v1 as components

# Session state to track user login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# Function to handle login
def sign_in():
    username = st.session_state.username
    password = st.session_state.password
    if username and password:  # Simple check
        st.session_state.logged_in = True

# Helper function to load HTML and CSS
def load_html_css(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# App logic based on login status
if st.session_state.logged_in:
    # Load dashboard (index.html)
    html_code = load_html_css("index.html")
    css_code = load_html_css("static/Sidebar.css")
    
    # Embed HTML and CSS into Streamlit
    components.html(f"""
        <style>{css_code}</style>
        {html_code}
    """, height=800)

else:
    st.header("Sign In to Pattchez")
    st.text_input("Username", key="username")
    st.text_input("Password", type="password", key="password")

    if st.button("Sign In"):
        sign_in()

    # Load and show sign-in page
    html_code = load_html_css("signup_in.html")
    css_code = load_html_css("static/mainpage.css")
    
    components.html(f"""
        <style>{css_code}</style>
        {html_code}
    """, height=600)
