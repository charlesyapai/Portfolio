import streamlit as st
import streamlit.components.v1 as components

# Specify html code below
components.html(
    """
    <style>
        .multicolor {
            font-family: Arial, sans-serif;
            background-image: url('path/to/your/image.jpg');
            background-clip: text;
            -webkit-background-clip: text;
            color: transparent;
        }

        .big-blue {
            font-family: Arial, sans-serif;
            font-size: 24px;
            color: blue;
        }

        .cursive-red {
            font-family: cursive;
            color: red;
        }
    </style>
    <h1> My Portfolio </h1>
    <div> I am a junior data scientist specializing in Python and Machine Learning.</div>
    <hr />
    <div> Project 1 - <a href="https://github.com/GryphonHolder/Project_1" target="_blank">GitHub Link</a> </div>
    <div> Project 2 - <a href="https://github.com/GryphonHolder/GAProj2" target="_blank">GitHub Link</a> </div>
    <div class="multicolor">Multicolor Text</div>
    <div class="big-blue">Big and Blue Text</div>
    <div class="cursive-red">Cursive and Red Text</div>
    """,
    height=600,
)



