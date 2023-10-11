# Face Recognition

Face Recognition is a function of CodeProjec.AI Server that allows you to recognize a face in a facial dataface that returns similarity index.

To use "codeproject" you must make web requests to the API. Here is an example of Face Recognition request.

This instructions assumes that you have [Postman](https://github.com/hugoescalpelo/data-visualization/blob/main/Postman/postman-documentation.md) installed and previously registered faces.

## Instructions

- Open [Postman](https://github.com/hugoescalpelo/data-visualization/blob/main/Postman/postman-documentation.md#install-postman).
    ```
    postman
    ```
- Create a new request by clicking in + icon.
- Change Method to **POST**.
- Change **URL** to ```http://localhost:32168/v1/vision/face/recognize```
- Clic on the **body** tab.
- Add a key called *image* with *file* type and browse for a picture with a face in it. For this example [spielberg2.png](https://github.com/hugoescalpelo/data-visualization/blob/main/faces/test_faces/spielberg2.png) is used. That file is already in this repository.
- Add a key called *min_confidence* and set a value between 0.0 and 1.0, for this example 0.6 will be used.
- Clic on  the **Send** button.
- If everything goes Ok, you will see the following result.
    ```
    {
    "message": "A face was recognised",
    "count": 1,
    "predictions": [
        {
            "confidence": 0.6179622262716293,
            "userid": "Steven Spielberg",
            "x_min": 86,
            "y_min": 82,
            "x_max": 310,
            "y_max": 430
        }
    ],
    "success": true,
    "inferenceMs": 23,
    "processMs": 36,
    "code": 200,
    "command": "recognize",
    "moduleId": "FaceProcessing",
    "executionProvider": "CUDA",
    "analysisRoundTripMs": 40
    }
    ```
As you can see, many useful values are returned, as count, coordinates and confidence.

![](https://github.com/hugoescalpelo/data-visualization/blob/main/Images/Screenshot%20from%202023-10-10%2017-58-48.png?raw=true)
## Reference

- [CodeProject.AI Server - Face Detection API Reference](https://www.codeproject.com/ai/docs/api/api_reference.html#face-detection)
