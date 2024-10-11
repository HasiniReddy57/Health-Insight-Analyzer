# Health Insight Analyzer: AI-Powered Medical Image Analysis

This Streamlit app leverages Google Generative AI's Gemini model to analyze medical images and provide insights into potential health conditions.

## Features:

- Upload a single medical image (PNG, JPG, JPEG)
- Analyze the image using a pre-trained AI model
- Receive a detailed report outlining potential findings and recommendations

**Important Disclaimer:** This app provides preliminary insights and should not be considered as medical advice. Always consult a healthcare professional for a comprehensive evaluation and treatment plan.

## Getting Started:

### Prerequisites:

- Python 3.x
- Streamlit (`pip install streamlit`)
- Google Generative AI API Key (obtain from Google Cloud Console)

### Clone the Repository:

```bash
git clone https://github.com/HasiniReddy57/Health-Condition-Prediction-App.git
```

### Create an API Key:

Follow the instructions on the Google Generative AI documentation to create an API key. Save the API key in a file named `api_key.py` within the project directory.

```python
apikey = "<your-api-key>"
```

### Run the App:

```bash
streamlit run app.py
```

## Tech Stack

### Frontend:
- **Streamlit**: A Python-based web framework used for building and deploying interactive user interfaces. It provides components for file upload, buttons, and displaying text and images.

### Backend:
- **Python**: The primary programming language used to develop the application.
- **Google Generative AI (Gemini Model)**: A pre-trained AI model from Google Generative AI, used to analyze the uploaded medical images and generate insights.
- **Tempfile**: A Python standard library module used to create temporary files for securely handling uploaded images.

### APIs and Integration:
- **Google Generative AI API**: Interacts with the Gemini model for medical image analysis. Requires an API key for authentication and authorization.

### Design and Styling:
- **Custom CSS**: Embedded within the Streamlit app for styling UI elements such as titles, subheaders, buttons, and the footer.

### Additional Libraries and Tools:
- **Tempfile**: Used for handling temporary file storage during image processing.

### Version Control and Collaboration:
- **Git**: Used for version control, facilitating collaboration and contribution to the project repository.



## Disclaimer:

This is a showcase application and not intended for medical diagnosis. Always consult a healthcare professional for any health concerns.

## Further Development:

- Enhance the summary generation logic for a more comprehensive overview of responses.
- Explore integrating additional functionalities like image pre-processing or visualization tools.
- Consider implementing a user interface for uploading multiple images.

## Demonstration Video
Check out this demonstration video to see Health Insight Analyzer in action!

[![Touch-Feedback-for-Virtual-Reality/Assets/Spinoverse.png](https://github.com/HasiniReddy57/Touch-Feedback-for-Virtual-Reality/blob/main/Assets/Spinoverse.png)](https://drive.google.com/file/d/1NQIL3MsY1MfwYd5NgHR7iM7MOYJ7xqmY/view)

In this video, you can see how real-time interactions work within the VR meeting rooms, as well as a demonstration of the touch feedback system using ESP32-driven haptic devices.

## Contributing
**Feel free to contribute or extend this project! Follow the below steps to proceed:**

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE]() file for details.
