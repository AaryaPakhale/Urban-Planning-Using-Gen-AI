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
        background-image: url('https://www.creativefabrica.com/wp-content/uploads/2020/03/08/City-with-apartment-and-shooping-mall-Graphics-3366119-1.jpg '); /* Background image URL */
        background-size: cover; /* Cover the whole area */
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    .stTextInput, .stButton {
        background-color: rgba(0, 0, 0, 0.8); /* Input boxes background */
        border: 1px solid #c23e9d; /* Input boxes border */
        border-radius: 5px; /* Rounded corners */
        color: white; 
    }
    .stTextInput:focus, .stButton:hover {
        background-color: rgba(255, 255, 255, 1); /* Input boxes background on focus */
        border-color: #7500c0; /* Border color on focus */
    }
    .select-amenities-label {
        font-weight: bold; /* Make text bold */
        font-size: 20px; /* Increase font size by 5 units (assuming the base size is 15px) */
        color: black; /* Set text color to black */
        margin-bottom: 5px;
    }
    .creator-links {
        display: flex;
        justify-content: space-around;
        padding: 20px 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit app interface
st.markdown('<h1 class="title">Optimize City Planning Solution</h1>', unsafe_allow_html=True)

# # File uploader for image input
# uploaded_file = st.file_uploader("Upload an image", type=['png', 'jpg', 'jpeg'])

# Text input for prompt
prompt = st.text_input("Enter your prompt")
# Text input for Budget
# budget = st.text_input("Enter your budget")

# # Text input for prompt
# prompt = st.text_input("Enter your prompt")

# Text input for city
city = st.text_input("Enter the city")

# Dropdown for amenities
amenities = st.selectbox("Select Amenities", [Hospital
School: amenity=school
University: amenity=university
Kindergarten: amenity=kindergarten
Library: amenity=library
Post Office: amenity=post_office
Police Station: amenity=police
Fire Station: amenity=fire_station
Community Center: amenity=community_centre
Pharmacy: amenity=pharmacy
Restaurant: amenity=restaurant
Café: amenity=cafe
Bar: amenity=bar
Supermarket: amenity=supermarket
Bank: amenity=bank
Atm: amenity=atm
Gym: amenity=gym
Park: amenity=park
Public Toilet: amenity=toilets
Bus Station: amenity=bus_station
Train Station: amenity=train_station
Airport: aeroway=aerodrome
Tourist Information: amenity=tourist_information
Waste Disposal: amenity=waste_basket
Dog Park: amenity=dog_park
Bicycle Rental: amenity=bicycle_rental
Hotel: amenity=hotel
Motel: amenity=motel
Camping: amenity=camp_site
Beach: amenity=beach])

# Button to get city planning suggestions
if st.button("Get City Planning Suggestions"):
    if uploaded_file is not None and prompt:
        # Convert image to bytes
        image_bytes = uploaded_file.read()
        
        # Insert data into database
        insert_data(image_bytes, prompt)
        
        st.success("Data submitted successfully!")
    else:
        st.error("Please upload an image and enter a prompt.")
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
            
        map_image_path = get_google_maps_image(city)
        # Pass the path to the image instead of its content
        suggestions, coordinates = get_city_planning_suggestions(prompt, map_image_path) 
        
        image = cv2.imread(map_image_path) 
        highlighted_image = highlight_pixels(image, coordinates)
        
        # Remove the temporary file after use
        os.remove(temp_image_path)
        st.write("City Planning Suggestions:")
        st.write(suggestions)
        st.image(highlighted_image, caption='Final Map', use_column_width=True)
        
    else:
        st.error("Please enter a prompt to get suggestions.")
st.markdown("""
<div class="creator-links">
    <div>
        <a href="https://github.com/NisargBhavsar25" target="_blank">Nisarg Bhavsar</a> | 
        <a href="https://www.linkedin.com/in/nisarg-bhavsar/" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/0/01/LinkedIn_Logo.svg" width="60" height="20">
        </a>
    </div>
    <div>
        <a href="https://github.com/AaryaPakhale" target="_blank">Aarya Pakhale</a> | 
        <a href="http://linkedin.com/in/aarya-pakhale-0b9788217" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/0/01/LinkedIn_Logo.svg" width="60" height="20">
        </a>
    </div>
    <div>
        <a href="https://github.com/meeranair186" target="_blank">Meera Nair</a> | 
        <a href="https://www.linkedin.com/in/meera-nair-8686ba259/" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/0/01/LinkedIn_Logo.svg" width="60" height="20">
        </a>
    </div>
    <div>
        <a href="https://github.com/Shreya6901" target="_blank">Shreya Singh</a> | 
        <a href="https://www.linkedin.com/in/singhshreya2003/" target="_blank">
            <img src="https://upload.wikimedia.org/wikipedia/commons/0/01/LinkedIn_Logo.svg" width="60" height="20">
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

# # Display stored images and prompts
# if st.button("Show Stored Data"):
#     conn = sqlite3.connect(DATABASE_NAME)
#     c = conn.cursor()
#     c.execute('SELECT * FROM images')
#     rows = c.fetchall()
    
#     for row in rows:
#         st.image(row[1], caption=f"Prompt: {row[2]}", use_column_width=True)

#     conn.close()
