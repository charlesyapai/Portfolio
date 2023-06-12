import streamlit as st
import streamlit.components.v1 as components

# Specify html code below
components.html(
    """
    <style>
        body {
            background-image: url('https://graduate.northeastern.edu/resources/wp-content/uploads/sites/4/2020/06/iStock-1221293664-1.jpg');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
    </style>
    <h1> My Portfolio </h1>
    <div> I am a junior data scientist specializing in Python and Machine Learning.</div>
    <hr />
    <div> Project 1 - <a href="https://github.com/GryphonHolder/Project_1" target="_blank">GitHub Link</a> </div>
    <div> Project 2 - <a href="https://github.com/GryphonHolder/GAProj2" target="_blank">GitHub Link</a> </div>
    """,
    height=600,
)
