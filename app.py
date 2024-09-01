import streamlit as st
import google.generativeai as genai
import tempfile
from api_key import apikey

# Configure the API key
genai.configure(api_key=apikey)

def upload_to_gemini(file_path, mime_type=None):
    """Uploads the given file to Gemini."""
    file = genai.upload_file(file_path, mime_type=mime_type)
    return file

# Define the model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Create the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-exp-0801",
    generation_config=generation_config,
    # Add safety settings if needed
)

# Refined prompt for image analysis
refined_prompt = """
As a highly skilled medical practitioner specializing in image analysis, you are tasked with examining medical images for a renowned hospital. Your experience is crucial in identifying any anomalies, diseases, or health issues that may be present in the images.

Your responsibilities include:

1. Detailed Analysis: Thoroughly analyze each image, focusing on identifying any abnormal findings.
2. Findings Report: Document all observed abnormalities or signs of disease. Clearly articulate these findings in a structured format.
3. Recommendations and Next Steps: Based on your analysis, suggest potential next steps, including further tests or treatments as applicable.
4. Treatment Suggestions: If appropriate, recommend possible treatment options or interventions.

Important Notes:

1. Scope of Response: Only respond if the image pertains to human health issues.
2. Clarity of Image: In cases where the image quality impedes clear analysis, note that certain aspects are 'Unable to be determined based on the provided image.'
3. Disclaimer: Accompany your analysis with the disclaimer: "Consult with a Doctor before making any decisions."

Your insights are invaluable in guiding clinical decisions. Please proceed with the analysis, adhering to the structured approach outlined above.
"""

# Streamlit UI setup
st.set_page_config(layout="centered", page_title="Health Insight Analyzer", page_icon=":robot:")

# Adding custom CSS for better styling
st.markdown("""
    <style>
    body {
        background-color: #1C1C1E;  /* Dark background for contrast */
    }
    .title {
        font-size: 2em;
        font-weight: bold;
        color: #76C7C0;  /* Calming teal for the title */
        text-align: center;
    }
    .subheader {
        font-size: 1.2em;
        color: #A6A6A6;  /* Soft grey for the subheader */
        text-align: center;
        margin-bottom: 30px;
    }
    .upload-btn {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    .stButton>button {
        background-color: #76C7C0;  /* Teal button color */
        color: #FFFFFF;  /* White text for contrast */
        border-radius: 8px;  /* Slightly rounded corners */
        padding: 0.75em 1.5em;  /* Padding for a more clickable button */
        font-size: 1em;  /* Larger font size for readability */
    }
    .stButton>button:hover {
        background-color: #63A5A0;  /* Slightly darker teal on hover */
    }
    .footer {
        text-align: center;
        font-size: 0.9em;
        color: #A6A6A6;  /* Soft grey for the footer text */
        margin-top: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Displaying the title and description
st.markdown('<div class="title">🔬 Health Insight Analyzer: AI-Powered Medical Image Analysis</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Unlock detailed insights into your health with advanced AI analysis. Upload your medical images to receive comprehensive evaluations and actionable recommendations tailored to your well-being.</div>', unsafe_allow_html=True)

# File uploader widget
st.markdown('<div class="upload-btn">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload your medical image to get insights about your condition", type=["png", "jpg", "jpeg"])
st.markdown('</div>', unsafe_allow_html=True)

# Analyze button
if st.button("Analyze my condition"):
    if uploaded_file is not None:
        # Save the uploaded file to a temporary location
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpeg") as temp_file:
            temp_file.write(uploaded_file.getbuffer())
            temp_file_path = temp_file.name

        # Upload the image file to Gemini
        try:
            file = upload_to_gemini(temp_file_path, mime_type="image/jpeg")
            
            # Define the chat history with the refined prompt
            prompt = [
                {
                    "role": "user",
                    "parts": [
                        file,  # the uploaded image file reference
                        refined_prompt
                    ],
                }
            ]
            
            # Start a chat session with the prompt
            chat_session = model.start_chat(history=prompt)
            
            # Send the message and get a response
            response = chat_session.send_message("Analyze my condition and suggest possible treatment")

            if response and hasattr(response, 'text'):
                st.image(uploaded_file, width=300, caption="Uploaded Image")
                st.write(response.text)
            else:
                st.error("No response received from the model.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please upload an image to analyze.")

# Footer with a disclaimer
st.markdown('<div class="footer">* This app provides preliminary insights and should not be considered as medical advice. Always consult a healthcare professional for a comprehensive evaluation and treatment plan.</div>', unsafe_allow_html=True)
