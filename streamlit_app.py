import streamlit as st
import random

st.set_page_config(layout="centered", page_title="F4 Poster Prompt Generator")

# HTML & CSS to mimic vertical F4 poster
st.markdown(
    """
    <style>
    .f4-poster-box {
        width: 400px;
        height: 570px;
        padding: 40px;
        margin: auto;
        border: 2px solid #ccc;
        border-radius: 10px;
        background: #fefefe;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .poster-title {
        text-align: center;
        font-size: 28px;
        margin-bottom: 20px;
    }
    .poster-section {
        margin-bottom: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

topics = [
    "A social message you care about",
    "An event you’d like to promote",
    "Something about your city that needs more attention",
    "A small act of resistance",
    "A message of joy or connection",
    "A strange or unexpected urban scene"
]

tone_prompts = [
    "Should the poster be loud or quiet?", 
    "Do you want to make people smile or think?",
    "Should it feel urgent or poetic?",
    "Is it personal or public?"
]

visual_prompts = [
    "Choose one image you’ve seen recently that stayed in your mind.",
    "What color do you associate with this message?",
    "Would it be more powerful as a photo, a drawing, or something abstract?",
    "Which part of the city would this poster live in?"
]

st.title("🎨 F4 Poster Prompt Generator")

st.write("Click below to get a serendipitous poster idea—styled as a concept card.")

if st.button("Generate Poster Idea"):
    topic = random.choice(topics)
    tone = random.choice(tone_prompts)
    visual = random.choice(visual_prompts)

    st.markdown(f"""
    <div class="f4-poster-box">
        <div class="poster-title">🎨 Poster Concept Card</div>
        <div class="poster-section"><strong>Topic:</strong><br>{topic}</div>
        <div class="poster-section"><strong>Tone:</strong><br>{tone}</div>
        <div class="poster-section"><strong>Visual Cue:</strong><br>{visual}</div>
        <div class="poster-section"><strong>Your Sentence:</strong><br>___________</div>
    </div>
    """, unsafe_allow_html=True)
