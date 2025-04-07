import streamlit as st
import random
import textwrap

st.set_page_config(layout="centered")

st.markdown("""
    <style>
    .poster-box {
        width: 595px;
        height: 842px;
        background: linear-gradient(135deg, #f5f5f5, #e0e0e0);
        border: 4px solid black;
        padding: 40px;
        font-family: 'Helvetica Neue', sans-serif;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .poster-section {
        margin-bottom: 30px;
    }
    .poster-label {
        font-weight: bold;
        font-size: 20px;
    }
    .poster-text {
        font-size: 18px;
        margin-top: 8px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🧠 F4 Poster Prompt Generator")
st.write("Click below to get a serendipitous poster idea—styled as a concept card.")

# Poster content lists
topics = [
    "A social message you care about",
    "An event you’d like to promote",
    "Something about your city that needs more attention",
    "A small act of resistance",
    "A message of joy or connection",
    "A strange or unexpected urban scene"
]

tone_prompts = [
    "Should the tone be loud or quiet?", 
    "Do you want to make people smile or think?",
    "Should it feel urgent or poetic?",
    "Is this message personal or collective?"
]

visual_prompts = [
    "What color or texture fits this idea best?",
    "Would it be more powerful as a photo, a drawing, or something abstract?",
    "Where in the city would this poster live best?",
    "Which mood should it evoke at first glance?"
]

prompt_builder = [
    "What is your core message in a sentence?",
    "Can you write a short prompt for MidJourney to visualize it?",
    "Is there a reference image, artist, or style you'd like to draw from?",
    "Try phrasing it like: 'A poster showing [theme] in the style of [reference] --ar 128:89'"
]

def generate_poster():
    topic = random.choice(topics)
    tone = random.choice(tone_prompts)
    visual = random.choice(visual_prompts)
    builder = random.choice(prompt_builder)

    st.markdown("""
        <div class="poster-box">
            <div class="poster-section">
                <div class="poster-label">🧭 Topic:</div>
                <div class="poster-text">{}</div>
            </div>
            <div class="poster-section">
                <div class="poster-label">🎯 Tone Question:</div>
                <div class="poster-text">{}</div>
            </div>
            <div class="poster-section">
                <div class="poster-label">🎨 Visual Suggestion:</div>
                <div class="poster-text">{}</div>
            </div>
            <div class="poster-section">
                <div class="poster-label">🧵 Prompt Seed:</div>
                <div class="poster-text">{}</div>
            </div>
        </div>
    """.format(topic, tone, visual, builder), unsafe_allow_html=True)

if st.button("Generate Poster Idea"):
    generate_poster()
