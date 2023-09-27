import streamlit as st
import pandas as pd

def career():
    st.title("🛣️ Career so far")
    with st.expander("❇️ IMAGINORLABS PRIVATE LIMITED"):
        st.link_button("Website","https://imaginorlabs.com/")
        st.link_button("More About Company","https://www.ynos.in/products/startups/index.html#!/dashboard?query=ImaginorLabs")
        st.caption("Role : Python Developer")
        st.caption("Sep 2022 - Mar 2023")

        ex1,ex2,ex3 = st.columns(3)

        with ex1:
            st.write("❥ Aided development of Click2tally,It is a web application that extracts invoice data and sends it to tally software. It uses Django framework to handle the user interface and the backend logic. It also uses yolov5 model to analyze the invoice layout and tesseract OCR software to extract the text from the images. The extracted data is shown on the website as tables and columns, and the user can edit it if needed.")

        with ex2:
            st.write("❥ Developed the Django backend that handles the user input, communicates with the API, parses the JSON response and renders the invoice data in the original layout. Annotated around 500 - 700 images for training the yolov5 model. Conducted the initial yolov5 training and assisted the CTO with optimization.")

        with ex3:
            st.write("❥ It extracts invoice data from images and sends it to tally software. It uses Django framework for the user interface and the backend logic. It uses yolov5 model to analyze the invoice layout and tesseract OCR software to extract the text from the images. It shows the extracted data on the website as tables and columns, and allows the user to edit it if needed.")

    with st.expander("☁️ Google Developer Student Club SRMEEC"):
        st.link_button("Website","https://gdsc.community.dev/easwari-engineering-college-chennai/")
        st.caption("Role : Cloud Lead")
        st.caption("Sep 2023 - Present")
        ex1,ex2,ex3 = st.columns(3)

        
        with ex1:
        
            st.write("❥ I conduct and overlook cloud related events by GDSC EEC")

def acheivements():
    st.title("Acheivements")
    df = pd.DataFrame(
    {
        "name": ["NIT Datronix Hackathon", "IBC media ALT Hack"],
        "position": ["Special Prize", "3rd Place"],
        "for what": ["Gesture Controlled Mouse","Decentralized Rewards App UVDrive"],
        "link": ["https://github.com/0EnIgma1/Gesture-Mouse_GCC_2.0","NIL"],
    }
)

    st.dataframe(df,hide_index=True)
        
