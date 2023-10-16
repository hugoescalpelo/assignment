import os
import cv2

# Set the path to the folder containing images
input_path = "/home/hugo/Documents/GitHub/data-visualization/faces/deepface_db"

# Create a cascades classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Iterate through all files and subdirectories in the input path
for root, dirs, files in os.walk(input_path):
    for file in files:
        if file.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):

            # Load the image
            image_path = os.path.join(root, file)
            image = cv2.imread(image_path)

            # Convert the image to grayscale for face detection
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Detect faces in the image
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

            # Process each detected face
            for i, (x, y, w, h) in enumerate(faces):
                # Crop the image to the detected face while maintaining proportion
                aspect_ratio = w / h
                new_height = 100
                new_width = int(aspect_ratio * new_height)
                face_cropped = image[y:y + h, x:x + w]
                resized_face = cv2.resize(face_cropped, (new_width, new_height))

                # Save the cropped face as 'face.jpg' in the same directory
                output_dir = os.path.dirname(image_path)
                output_path = os.path.join(output_dir, 'face.jpg')
                cv2.imwrite(output_path, resized_face)

                print(f"Processed and saved face in {output_path}")

print("Face detection and cropping completed.")
