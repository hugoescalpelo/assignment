from deepface import DeepFace

obj = DeepFace.analyze (img_path = "/home/hugo/Documents/GitHub/data-visualization/deepface/samples/capture.jpg", actions = ['age', 'gender', 'race', 'emotion'])

print ("Analysis results are: ")
print (obj)