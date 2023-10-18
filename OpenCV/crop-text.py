import cv2
import argparse
import os

# Parser
parser = argparse.ArgumentParser()
parser.add_argument("img_path", help="Path to the image to process")
parser.add_argument("index", type=int, help="Index for the image")
parser.add_argument("x_min", type=int, help="Minimum X-coordinate")
parser.add_argument("x_max", type=int, help="Maximum X-coordinate")
parser.add_argument("y_min", type=int, help="Minimum Y-coordinate")
parser.add_argument("y_max", type=int, help="Maximum Y-coordinate")
args = parser.parse_args()

# Load the image
image = cv2.imread(args.img_path)

# Define the coordinates
x_min, x_max, y_min, y_max = args.x_min, args.x_max, args.y_min, args.y_max

# Crop the image
cropped = image[y_min:y_max, x_min:x_max]

# Calculate the new width to maintain proportion with a fixed height of 100 pixels
new_width = int(100 * (x_max - x_min) / (y_max - y_min))
new_height = 100  # Fixed height of 100 pixels

# Resize the image while maintaining the proportion
resized = cv2.resize(cropped, (new_width, new_height))

# Generate the output filename based on the index
output_filename = f'/home/hugo/Pictures/img{args.index}.jpg'

# Save the processed image
cv2.imwrite(output_filename, resized)

# print(f"Processed image saved as: {output_filename}")
