import os
import streamlit as st

# Get the absolute path to the CSS file
css_path = os.path.join(os.path.dirname(__file__), 'styles.css')

# Refer to the CSS file using st.markdown
st.markdown(f'<link href="{css_path}" rel="stylesheet">', unsafe_allow_html=True)

# Your remaining Streamlit code
st.title("My Portfolio")
st.write("I am a junior data scientist specializing in Python and Machine Learning.")
st.write("Project 1 - [GitHub Link](https://github.com/GryphonHolder/Project_1)")
st.write("Project 2 - [GitHub Link](https://github.com/GryphonHolder/GAProj2)")
