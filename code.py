import streamlit as st
import streamlit.components.v1 as components

# Specify html code below
components.html(
    """
    <style>
        .multicolor {
            font-family: Arial, sans-serif;
            background-image: url('https://graduate.northeastern.edu/resources/wp-content/uploads/sites/4/2020/06/iStock-1221293664-1.jpg');
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

        .section {
            padding: 50px 0;
        }

        .section h2 {
            margin-bottom: 30px;
        }

        .project {
            margin-bottom: 20px;
        }
    </style>
    <h1> Charles "Prof" Yap </h1>
    <h2> Aspiring Data Scientist </h2>
    <hr />

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
        <h2>Showcase</h2>
        <p>Here you can showcase your work and graphs. You can use JavaScript to make this section interactive.</p>
    </div>

    <div class="section">
        <h2>Contact</h2>
        <p>If you would like to get in touch, please contact me at <a href="mailto:your-email@example.com">your-email@example.com</a>.</p>
    </div>

    height=600,
)
