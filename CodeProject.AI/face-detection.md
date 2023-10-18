# Face Detection

Face detection is a function of CodeProjec.AI Server that allows you to check if a face is in a picture file.

To use **CodeProject.AI Server** you must make web requests to the API. Here is an example of Face Detection request.

This instructions assumes that you have [Postman](https://github.com/hugoescalpelo/data-visualization/blob/main/Postman/postman-documentation.md) installed and a picture with a face in it.

## Instructions

- Open [Postman](https://github.com/hugoescalpelo/data-visualization/blob/main/Postman/postman-documentation.md#install-postman).
    ```
    postman
    ```
- Create a new request by clicking in + icon.
- Change Method to **POST**.
- Change **URL** to ```http://localhost:32168/v1/vision/face```
- Clic on the **body** tab.
- Add a key called *image* with *file* type and browse for a picture with a face in it.
- Add a key called *min_confidence* and assign a value of **0.4**.
- Clic on  the **Send** button.
- If everything goes Ok, you will see the following result.
    ```
    {
        "success": true,
        "predictions": [
            {
                "confidence": 0.9011256098747253,
                "x_min": 207,
                "y_min": 112,
                "x_max": 416,
                "y_max": 386
            }
        ],
        "count": 1,
        "message": "Found 1 face",
        "inferenceMs": 31,
        "processMs": 32,
        "code": 200,
        "command": "detect",
        "moduleId": "FaceProcessing",
        "executionProvider": "CUDA",
        "analysisRoundTripMs": 36
    }
    ```
![](https://github.com/hugoescalpelo/data-visualization/blob/main/Images/Screenshot%20from%202023-10-10%2016-09-11.png?raw=true)
## Reference

- [CodeProject.AI Server - Face Detection API Reference](https://www.codeproject.com/ai/docs/api/api_reference.html#face-detection)

