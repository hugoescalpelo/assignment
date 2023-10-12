from deepface import DeepFace

print ("Comparing 2 images ")

# result = DeepFace.verify(img1_path = "img1.jpg", img2_path = "img2.jpg")
result = DeepFace.verify(img1_path = "/home/hugo/Documents/GitHub/data-visualization/deepface/samples/capture.jpg", img2_path = "/home/hugo/Documents/GitHub/data-visualization/deepface/samples/capture02.jpg")

print ("Results")
print (result)