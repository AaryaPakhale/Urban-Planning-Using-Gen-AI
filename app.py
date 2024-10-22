# import streamlit as st
# from PIL import Image
# import sqlite3
# import os
# from vlm import get_city_planning_suggestions
# from openstreetmap_api import save_colored_city_map
# import cv2

# # Set up the SQLite database
# DATABASE_NAME = 'city_planning.db'

# # def create_table():
# #     conn = sqlite3.connect(DATABASE_NAME)
# #     c = conn.cursor()
# #     c.execute('''CREATE TABLE IF NOT EXISTS images
# #                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
# #                  image BLOB,
# #                  prompt TEXT)''')
# #     conn.commit()
# #     conn.close()

# # Function to create the table
# def create_table():
#     conn = sqlite3.connect(DATABASE_NAME)
#     c = conn.cursor()
#     # Creating table with columns prompt, city, and amenities
#     c.execute('''
#         CREATE TABLE IF NOT EXISTS city_data (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             prompt TEXT,
#             city TEXT,
#             amenities TEXT
#         )
#     ''')
#     conn.commit()
#     conn.close()

# def insert_data(prompt, city, amenities):
#     conn = sqlite3.connect(DATABASE_NAME)
#     c = conn.cursor()
#     # Inserting values into the table
#     c.execute('INSERT INTO city_data (prompt, city, amenities) VALUES (?, ?, ?)', (prompt, city, amenities))
#     conn.commit()
#     conn.close()
    
# # Create the table if it doesn't exist
# create_table()

# # Custom CSS for styling
# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-image: url('https://www.creativefabrica.com/wp-content/uploads/2020/03/08/City-with-apartment-and-shooping-mall-Graphics-3366119-1.jpg '); /* Background image URL */
#         background-size: cover; /* Cover the whole area */
#         background-repeat: no-repeat;
#         background-attachment: fixed;
#     }
#     .stTextInput, .stButton {
#         background-color: rgba(0, 0, 0, 0.8); /* Input boxes background */
#         border: 1px solid #c23e9d; /* Input boxes border */
#         border-radius: 5px; /* Rounded corners */
#         color: white; 
#     }
#     .stTextInput:focus, .stButton:hover {
#         background-color: rgba(255, 255, 255, 1); /* Input boxes background on focus */
#         border-color: #7500c0; /* Border color on focus */
#     }
#     .select-amenities-label {
#         font-weight: bold; /* Make text bold */
#         font-size: 20px; /* Increase font size by 5 units (assuming the base size is 15px) */
#         color: black; /* Set text color to black */
#         margin-bottom: 5px;
#     }
#     .creator-links {
#         display: flex;
#         justify-content: space-around;
#         padding: 20px 0;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Streamlit app interface
# st.markdown('<h1 class="title">Optimize City Planning Solution</h1>', unsafe_allow_html=True)

# # # File uploader for image input
# # uploaded_file = st.file_uploader("Upload an image", type=['png', 'jpg', 'jpeg'])

# # Text input for prompt
# prompt = st.text_input("Enter your Problem")
# # Text input for Budget
# # budget = st.text_input("Enter your budget")

# # # Text input for prompt
# # prompt = st.text_input("Enter your prompt")

# # Text input for city
# city = st.text_input("Enter the City")

# # Dropdown for amenities
# amenities = st.selectbox("Select Amenities", ["Hospital",
# "School",
# "University",
# "Kindergarten",
# "Library",
# "Post_office",
# "Police",
# "Fire_station",
# "Community_centre",
# "Pharmacy",
# "Restaurant",
# "Cafe",
# "Bar",
# "Supermarket",
# "Bank",
# "Atm",
# "Gym",
# "Park",
# "Toilets",
# "Bus_station",
# "Train_station",
# "Aerodrome",
# "Tourist_information",
# "Waste_basket",
# "Dog_park",
# "Bicycle_rental",
# "Hotel",
# "Motel",
# "Camp_site",
# "Beach"])

# # Button to get city planning suggestions
# if st.button("Get City Planning Suggestions"):
#     if (prompt and city and amenities):
#         # Convert image to bytes
#         # image_bytes = uploaded_file.read()
        
#         # Insert data into database
#         insert_data(prompt, city, amenities)
#         st.success("Data submitted successfully!")
        
#         map_image_path = "city_colored_map_with_amenities.jpg"
#         save_colored_city_map(city, amenities, filename=map_image_path)
        
#         # Pass the path to the image instead of its content
#         suggestions, coordinates = get_city_planning_suggestions(prompt, map_image_path) 
        
#         image = cv2.imread(map_image_path) 
#         highlighted_image = highlight_pixels(image, coordinates)
        
#         # Remove the temporary file after use
#         os.remove(temp_image_path)
#         st.write("City Planning Suggestions:")
#         st.write(suggestions)
#         st.image(highlighted_image, caption='Final Map', use_column_width=True)
        
#     else:
#         st.error("Please enter a valid prompt, city and amenity.")
        
#     # if prompt:
#     #     conn = sqlite3.connect(DATABASE_NAME)
#     #     c = conn.cursor()
#     #     c.execute('SELECT * FROM images')
#     #     rows = c.fetchall()
#     #     row = rows[-1]
#         # st.image(row[1], caption=f"Prompt: {row[2]}", use_column_width=True)
#         # Save the image to a temporary file
#         # temp_image_path = os.path.join("temp_image.png")
#         # with open(temp_image_path, "wb") as f:
#         #     f.write(row[1])
        
# st.markdown("""
# <div class="creator-links">
#     <div>
#         <a href="https://github.com/NisargBhavsar25" target="_blank">Nisarg Bhavsar</a> | 
#         <a href="https://www.linkedin.com/in/nisarg-bhavsar/" target="_blank">
#             <img src="https://upload.wikimedia.org/wikipedia/commons/0/01/LinkedIn_Logo.svg" width="60" height="20">
#         </a>
#     </div>
#     <div>
#         <a href="https://github.com/AaryaPakhale" target="_blank">Aarya Pakhale</a> | 
#         <a href="http://linkedin.com/in/aarya-pakhale-0b9788217" target="_blank">
#             <img src="https://upload.wikimedia.org/wikipedia/commons/0/01/LinkedIn_Logo.svg" width="60" height="20">
#         </a>
#     </div>
#     <div>
#         <a href="https://github.com/meeranair186" target="_blank">Meera Nair</a> | 
#         <a href="https://www.linkedin.com/in/meera-nair-8686ba259/" target="_blank">
#             <img src="https://upload.wikimedia.org/wikipedia/commons/0/01/LinkedIn_Logo.svg" width="60" height="20">
#         </a>
#     </div>
#     <div>
#         <a href="https://github.com/Shreya6901" target="_blank">Shreya Singh</a> | 
#         <a href="https://www.linkedin.com/in/singhshreya2003/" target="_blank">
#             <img src="https://upload.wikimedia.org/wikipedia/commons/0/01/LinkedIn_Logo.svg" width="60" height="20">
#         </a>
#     </div>
# </div>
# """, unsafe_allow_html=True)

# # # Display stored images and prompts
# # if st.button("Show Stored Data"):
# #     conn = sqlite3.connect(DATABASE_NAME)
# #     c = conn.cursor()
# #     c.execute('SELECT * FROM images')
# #     rows = c.fetchall()
    
# #     for row in rows:
# #         st.image(row[1], caption=f"Prompt: {row[2]}", use_column_width=True)

# #     conn.close()



import streamlit as st
from PIL import Image
import sqlite3
import os
import cv2
from vlm import get_city_planning_suggestions
from openstreetmap_api import save_colored_city_map

# Set up the SQLite database
DATABASE_NAME = 'city_planning.db'

# Function to create the table
def create_table():
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    # Creating table with columns prompt, city, and amenities
    c.execute('''
        CREATE TABLE IF NOT EXISTS city_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prompt TEXT,
            city TEXT,
            amenities TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_data(prompt, city, amenities):
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    # Inserting values into the table
    c.execute('INSERT INTO city_data (prompt, city, amenities) VALUES (?, ?, ?)', (prompt, city, amenities))
    conn.commit()
    conn.close()

# Create the table if it doesn't exist
create_table()

# Streamlit app interface
st.markdown('<h1 class="title">Optimize City Planning Solution</h1>', unsafe_allow_html=True)

# Text input for prompt
prompt = st.text_input("Enter your Problem")

# Text input for city
city = st.text_input("Enter the City")

# Dropdown for amenities
amenities = st.selectbox("Select Amenities", [
    "Hospital", "School", "University", "Kindergarten", "Library", 
    "Post_office", "Police", "Fire_station", "Community_centre", 
    "Pharmacy", "Restaurant", "Cafe", "Bar", "Supermarket", "Bank",
    "Atm", "Gym", "Park", "Toilets", "Bus_station", "Train_station",
    "Aerodrome", "Tourist_information", "Waste_basket", "Dog_park", 
    "Bicycle_rental", "Hotel", "Motel", "Camp_site", "Beach"
])

# Button to get city planning suggestions
if st.button("Get City Planning Suggestions"):
    if (prompt and city and amenities):
        # Insert data into the database
        insert_data(prompt, city, amenities)
        st.success("Data submitted successfully!")
        
        map_image_path = "city_colored_map_with_amenities.jpg"
        
        # Try saving the city map with amenities and railways
        try:
            image = save_colored_city_map(city, amenities, filename=map_image_path)
            st.image(image, caption=f"Map of {city} with {amenities}", use_column_width=True)
        except Exception as e:
            st.error(f"Error generating map: {e}")
            st.stop()
        
        # Now, get city planning suggestions based on the image and prompt
        try:
            suggestions, coordinates = get_city_planning_suggestions(prompt, map_image_path)
            image = cv2.imread(map_image_path)
            highlighted_image = highlight_pixels(image, coordinates)  # Ensure this function is defined
            st.image(highlighted_image, caption='Highlighted City Planning Map', use_column_width=True)
            st.write("City Planning Suggestions:")
            st.write(suggestions)
        except Exception as e:
            st.error(f"Error processing city planning suggestions: {e}")
        
    else:
        st.error("Please enter a valid prompt, city, and amenity.")

# Footer links
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

