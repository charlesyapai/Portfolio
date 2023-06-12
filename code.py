import streamlit as st
import streamlit.components.v1 as components

# Specify html code below
components.html(
    """
    <style>
        body {
            background-color: #f4f4f4;
            font-family: Arial, sans-serif;
        }

        .header {
            text-align: center;
            padding: 50px;
            background-color: #333;
            color: white;
        }

        .section {
            padding: 50px 0;
            text-align: center;
        }

        .section h2 {
            margin-bottom: 30px;
        }

        .project {
            margin-bottom: 20px;
        }

        .strengths, .weaknesses {
            display: flex;
            justify-content: space-around;
            margin-bottom: 20px;
        }

        .strengths div, .weaknesses div {
            width: 30%;
        }
    </style>
    <div class="header">
        <h1> Charles "Prof" Yap </h1>
        <h2> Aspiring Data Scientist </h2>
        <img src="https://your-image-url.com" alt="Your image" width="200">
    </div>

    <div class="section">
        <h2>About Me</h2>
        <p>I am a junior data scientist specializing in Python and Machine Learning. I have an interest in utilizing Machine learning to generate business insights.</p>
    </div>

    <div class="section">
        <h2>Projects</h2>
        <div class="project">
            <h3>Project 1</h3>
            <p>Description of Project 1.</p>
            <a href="https://github.com/GryphonHolder/Project_1" target="_blank">View on GitHub</a>
        </div>
        <div class="project">
            <h3>Project 2</h3>
            <p>Description of Project 2.</p>
            <a href="https://github.com/GryphonHolder/GAProj2" target="_blank">View on GitHub</a>
        </div>
    </div>

    <div class="section">
        <h2>Strengths</h2>
        <div class="strengths">
            <div>
                <h3>Strength 1</h3>
                <p>Description of Strength 1.</p>
            </div>
            <div>
                <h3>Strength 2</h3>
                <p>Description of Strength 2.</p>
            </div>
            <div>
                <h3>Strength 3</h3>
                <p>Description of Strength 3.</p>
            </div>
        </div>
    </div>

    <div class="section">
        <h2>Weaknesses</h2>
        <div class="weaknesses">
            <div>
                <h3>Weakness 1</h3>
                <p>Description of Weakness 1.</p>
            </div>
            <div>
                <h3>Weakness 2</h3>
                <p>Description of Weakness 2.</p>
            </div>
            <div>
                <h3>Weakness 3</h3>
                <p>Description of Weakness 3.</p>
            </div>
        </div>
    </div>

    <div class="section">
        <h2>Contact</h2>
        <p>If you would like to get in touch, please contact me at <a href="mailto:your-email@example.com">your-email@example.com</a>.</p>
    </div>
    """,
    height=600,
)
