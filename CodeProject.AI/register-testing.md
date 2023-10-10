# Face Registration

Face Registration is a function of CodeProjec.AI Server that allows you to register a face and then check for similarity.

To use "codeproject" you must make web requests to the API. Here is an example of Face Registration request.

This instructions assumes that you have [Postman](https://github.com/hugoescalpelo/data-visualization/blob/main/Postman/postman-documentation.md) installed and a picture with a face in it.

## Instructions

- Open [Postman](https://github.com/hugoescalpelo/data-visualization/blob/main/Postman/postman-documentation.md#install-postman).
    ```
    postman
    ```
- Create a new request by clicking in + icon.
- Change Method to **POST**.
- Change **URL** to ```http://localhost:32168/v1/vision/face/register```
- Clic on the **body** tab.
- Add a key called *imageN* with *file* type and browse for a picture with a face in it. Remember there is a facial database in [/data-visualization/faces/face_db/](https://github.com/hugoescalpelo/data-visualization/tree/main/faces/face_db) folder.
- Add a key called *userid* and write the name of the person registered.
- Clic on  the **Send** button.
- If everything goes Ok, you will see the following result.
    ```
    {
    "success": true,
    "message": "face added",
    "inferenceMs": 29,
    "processMs": 45,
    "code": 200,
    "command": "register",
    "moduleId": "FaceProcessing",
    "executionProvider": "CUDA",
    "analysisRoundTripMs": 48
    }
    ```


![](https://github.com/hugoescalpelo/data-visualization/blob/main/Images/Screenshot%20from%202023-10-10%2016-02-14.png?raw=true)
## Reference

- [CodeProject.AI Server - Face Detection API Reference](https://www.codeproject.com/ai/docs/api/api_reference.html#face-detection)
