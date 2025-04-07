
import streamlit as st
import random
from PIL import Image, ImageDraw, ImageFont
import io

# Set page layout
st.set_page_config(layout="centered")

# Poster categories and prompts
categories = {
    "Cultural Posters": [
        "A music festival in your town",
        "An open studio invitation",
        "A local film screening on a rooftop"
    ],
    "Political Messaging / Referendum": [
        "A poster for or against a city referendum",
        "A message about equal rights",
        "A call to vote for something you believe in"
    ],
    "City Announcements & Public Invitations": [
        "A lost & found city event",
        "Join your neighbors for an urban dinner",
        "A poster that announces nothing, but feels like it does"
    ],
    "Gender Equality / Inclusion / Care": [
        "A poster about everyday sexism",
        "A moment of care in the city",
        "An invitation to just be safe and seen"
    ],
    "Ecological Transitions / Commons": [
        "A message about shared green space",
        "A speculative climate future",
        "A call to save urban trees"
    ],
    "Anti-Ad / Media Literacy Posters": [
        "A poster that makes fun of advertising",
        "Something that reveals what we don't notice",
        "An anti-billboard billboard"
    ],
    "Dreamlike Urban Scenes": [
        "A poster from an imagined future",
        "A silent ritual in a public square",
        "A floating object appearing above the city"
    ]
}

colors = ["#f4e04d", "#f45b69", "#9fedd7", "#a28089", "#4a6fa5", "#ffb627"]

# Generate a poster idea
def generate_poster():
    category = random.choice(list(categories.keys()))
    idea = random.choice(categories[category])
    color = random.choice(colors)
    return category, idea, color

# Draw the poster
def draw_poster(category, idea, color):
    img = Image.new('RGB', (768, 512), color=color)
    draw = ImageDraw.Draw(img)

    try:
        font_cat = ImageFont.truetype("DejaVuSans-Bold.ttf", 24)
        font_idea = ImageFont.truetype("DejaVuSans.ttf", 20)
    except:
        font_cat = font_idea = None  # fallback in case fonts not available

    draw.text((30, 30), category, fill="black", font=font_cat)
    draw.text((30, 100), idea, fill="black", font=font_idea)

    return img

# UI
st.title("🎨 F4 Poster Prompt Generator")
st.markdown("Click below to get a serendipitous poster idea—styled as a concept card.")

if st.button("Generate Poster Idea"):
    cat, idea, color = generate_poster()
    poster = draw_poster(cat, idea, color)
    buf = io.BytesIO()
    poster.save(buf, format="PNG")
    st.image(buf.getvalue(), caption="Your F4 Poster Prompt", use_column_width=True)
    st.download_button("Download Poster", data=buf.getvalue(), file_name="poster_idea.png", mime="image/png")
