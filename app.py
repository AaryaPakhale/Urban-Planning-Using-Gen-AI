import streamlit as st
from PIL import Image
import sqlite3
import os
from vlm import get_city_planning_suggestions

# Set up the SQLite database
DATABASE_NAME = 'image_prompts.db'

def create_table():
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS images
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 image BLOB,
                 prompt TEXT)''')
    conn.commit()
    conn.close()

def insert_data(image, prompt):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute('INSERT INTO images (image, prompt) VALUES (?, ?)', (image, prompt))
    conn.commit()
    conn.close()

# Create the table if it doesn't exist
create_table()

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #c23e9d, #7500c0); /* Background gradient */
    }
    .stTextInput, .stButton {
        background-color: rgba(255, 255, 255, 0.8); /* Input boxes background */
        border: 1px solid #c23e9d; /* Input boxes border */
        border-radius: 5px; /* Rounded corners */
    }
    .stTextInput:focus, .stButton:hover {
        background-color: rgba(255, 255, 255, 1); /* Input boxes background on focus */
        border-color: #7500c0; /* Border color on focus */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit app interface
st.title("Image and Prompt Upload")

# File uploader for image input
uploaded_file = st.file_uploader("Upload an image", type=['png', 'jpg', 'jpeg'])

# Text input for prompt
prompt = st.text_input("Enter your prompt")

if st.button("Submit"):
    if uploaded_file is not None and prompt:
        # Convert image to bytes
        image_bytes = uploaded_file.read()
        
        # Insert data into database
        insert_data(image_bytes, prompt)
        
        st.success("Data submitted successfully!")
    else:
        st.error("Please upload an image and enter a prompt.")

# Display stored images and prompts
if st.button("Show Stored Data"):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute('SELECT * FROM images')
    rows = c.fetchall()
    
    for row in rows:
        st.image(row[1], caption=f"Prompt: {row[2]}", use_column_width=True)

    conn.close()

# Button to get city planning suggestions
if st.button("Get City Planning Suggestions"):
    if prompt:
        conn = sqlite3.connect(DATABASE_NAME)
        c = conn.cursor()
        c.execute('SELECT * FROM images')
        rows = c.fetchall()
        row = rows[-1]
        # st.image(row[1], caption=f"Prompt: {row[2]}", use_column_width=True)
        # Save the image to a temporary file
        temp_image_path = os.path.join("temp_image.png")
        with open(temp_image_path, "wb") as f:
            f.write(row[1])
        
        # Pass the path to the image instead of its content
        suggestions = get_city_planning_suggestions(prompt, temp_image_path)
        
        # Remove the temporary file after use
        os.remove(temp_image_path)
        st.write("City Planning Suggestions:")
        st.write(suggestions)
    else:
        st.error("Please enter a prompt to get suggestions.")