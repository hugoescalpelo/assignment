# OCR Testing
OCR is a function of CodeProjec.AI Server that allows you to recognize text inside an image and returns an array of texts detected and its coordinates.

To use **CodeProject.AI Server** you must make web requests to the API. Here is an example of FOCR request.

This instructions assumes that you have Postman installed and previously registered faces.

## Instructions

- Open [Postman](https://github.com/hugoescalpelo/data-visualization/blob/main/Postman/postman-documentation.md#install-postman).
    ```
    postman
    ```
- Create a new request by clicking in + icon.
- Change Method to **POST**.
- Change **URL** to ```http://localhost:32168/v1/image/ocr```
- Clic on the **body** tab.
- Add a key called *file* with *file* type and browse for a picture with a face in it.
- Clic on  the **Send** button.
- If everything goes Ok, you will see the following result.
    ```
    {
    "success": true,
    "predictions": [
        {
            "confidence": 0.995843768119812,
            "label": "Hugo",
            "x_min": 161,
            "y_min": 275,
            "x_max": 295,
            "y_max": 362
        },
        {
            "confidence": 0.9796797633171082,
            "label": "Escalpelo",
            "x_min": 164,
            "y_min": 350,
            "x_max": 340,
            "y_max": 407
        }
    ],
    "message": "2 pieces of text found",
    "processMs": 359,
    "inferenceMs": 358,
    "code": 200,
    "command": "ocr",
    "moduleId": "OCR",
    "executionProvider": "CPU",
    "analysisRoundTripMs": 367
    }
    ```
![](https://github.com/hugoescalpelo/data-visualization/blob/main/Images/Screenshot%20from%202023-10-17%2018-02-32.png?raw=true)
## Reference

- [CodeProject.AI Server - Face Detection API Reference](https://www.codeproject.com/ai/docs/api/api_reference.html#face-detection)

