from google_maps import get_google_maps_image
from vlm import get_city_planning_suggestions
from image_highlighting import highlight_pixels
import cv2

def process_location_and_suggestions(location, prompt):
    # Fetch map image from Google Maps
    map_image_path = get_google_maps_image(location)
    
    if map_image_path:
        # Get city planning suggestions and coordinates
        suggestions, coordinates = get_city_planning_suggestions(prompt, map_image_path)
        
        # Load the image and highlight the suggested areas
        image = cv2.imread(map_image_path)
        highlighted_image = highlight_pixels(image, coordinates)
        
        # Return both text suggestions and highlighted map image
        return suggestions, highlighted_image
    else:
        raise Exception("Failed to fetch map image")

# Example usage:
# location = "New York, USA"
# prompt = "The city has transportation issues, particularly traffic congestion in downtown areas."
# suggestions, highlighted_image = process_location_and_suggestions(location, prompt)
# print(suggestions)
# cv2.imshow('Highlighted Image', highlighted_image)
