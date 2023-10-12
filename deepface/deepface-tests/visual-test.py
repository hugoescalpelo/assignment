import matplotlib.pyplot as plt
from deepface import DeepFace

model_names = [
    "VGG-Face",
    "Facenet",
    "Facenet512",
    "OpenFace",
    "DeepFace",
    "DeepID",
    "Dlib",
    "ArcFace",
    "SFace",
]
detector_backends = ["opencv", "ssd", "mtcnn", "retinaface", "dlib"]

# verification
for model_name in model_names:
    obj = DeepFace.verify(
        img1_path="/home/hugo/Documents/GitHub/data-visualization/deepface/deepface-tests/dataset/img1.jpg", img2_path="/home/hugo/Documents/GitHub/data-visualization/deepface/deepface-tests/dataset/img2.jpg", model_name="DeepFace"
    )
    print(obj)
    print("---------------------")

# represent
for model_name in model_names:
    embedding_objs = DeepFace.represent(img_path="/home/hugo/Documents/GitHub/data-visualization/deepface/deepface-tests/dataset/img1.jpg", model_name="DeepFace")
    for embedding_obj in embedding_objs:
        embedding = embedding_obj["embedding"]
        print(f"{model_name} produced {len(embedding)}D vector")

# find
dfs = DeepFace.find(
    img_path="/home/hugo/Documents/GitHub/data-visualization/deepface/deepface-tests/dataset/img1.jpg", db_path="/home/hugo/Documents/GitHub/data-visualization/deepface/deepface-tests/dataset", model_name="Facenet", detector_backend="mtcnn"
)
for df in dfs:
    print(df)

# extract faces
for detector_backend in detector_backends:
    face_objs = DeepFace.extract_faces(
        img_path="/home/hugo/Documents/GitHub/data-visualization/deepface/deepface-tests/dataset/img1.jpg", detector_backend=detector_backend
    )
    for face_obj in face_objs:
        face = face_obj["face"]
        print(detector_backend)
        plt.imshow(face)
        plt.axis("off")
        plt.show()
        print("-----------")