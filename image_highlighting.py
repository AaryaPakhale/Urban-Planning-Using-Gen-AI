import cv2
import numpy as np

def highlight_pixels(image, pixel_coordinates, highlight_color=(0, 0, 255), radius=50):
    """
    Highlights specified pixels in an RGB image.

    Parameters:
    - image: The input RGB image as a NumPy array.
    - pixel_coordinates: A list of (x, y) tuples representing the pixel coordinates to highlight.
    - highlight_color: The color to use for highlighting, default is red (0, 0, 255).
    - radius: The radius of the circle to draw around the pixel.

    Returns:
    - The image with the highlighted pixels.
    """
    # Create a copy of the image to avoid modifying the original
    highlighted_image = image.copy()

    # Loop through all pixel coordinates and highlight them
    for (x, y) in pixel_coordinates:
        # Draw a circle around the pixel
        cv2.circle(highlighted_image, (x, y), radius, highlight_color, -1)

    return highlighted_image

# if __name__ == "__main__":
#     # Example usage
#     image_path = 'path_to_your_image/bhuvan_wms_map.png'  # Change this path
#     image = cv2.imread(image_path)

#     if image is None:
#         print("Error loading image.")
#     else:
#         # Specify pixel coordinates to highlight [(x1, y1), (x2, y2), ...]
#         pixel_coords = [(50, 50), (100, 200), (300, 400)]  # Example coordinates

#         # Call the function to highlight the pixels
#         highlighted_image = highlight_pixels(image, pixel_coords, highlight_color=(0, 0, 255), radius=50)

        # # Save or display the image
        # output_path = 'highlighted_image.jpg'
        # cv2.imwrite(output_path, highlighted_image)
        # print(f"Image saved at {output_path}")

        # # Display the image using OpenCV
        # cv2.imshow('Highlighted Image', highlighted_image)
        # cv2.waitKey(0)  # Press any key to close the window
        # cv2.destroyAllWindows()
