import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
from custom_html import GITHUB_PROFILE,LINKEDIN_PROFILE
from home_page import home_page
from stuff_i_know import stuff_i_know
from projects import projects
from blogs import blogs
from career import career,acheivements


st.sidebar.text("Arjun's Portfolio")


selected_page = st.sidebar.selectbox(
    "Select Page",
    ("🥸 Introduction", "💸 My Stack", "🔭 Projects","🚀 Blogs","🛣️ Career")
)

with st.sidebar:
    
    components.html(GITHUB_PROFILE)
    components.html(LINKEDIN_PROFILE,height=500,width=900)

    with open("static/resume.pdf", "rb") as file:
        btn = st.download_button(
                label="Download my resume",
                data=file,
                file_name="resume.pdf"
            )
    components.html("""📧<a href="mailto:arjunprakash027@gmail.com">arjunprakash027@gmail.com</a>
""")


if selected_page == "🥸 Introduction":
    home_page()

if selected_page == "💸 My Stack":
    stuff_i_know()

if selected_page == "🔭 Projects":
    projects()

if selected_page == "🚀 Blogs":
    blogs()

if selected_page == "🛣️ Career":
    career()
    acheivements()


