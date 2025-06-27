import streamlit as st
from PIL import Image
import openai
import io
import base64
import os

# Load OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_KEY")

# Streamlit UI
st.set_page_config(page_title="CNIC Extractor", page_icon="🪪")
st.title("🇵🇰 CNIC Information Extractor")
st.markdown("Upload a Pakistani CNIC image using **Camera or Gallery** to extract the details using AI.")

use_camera = st.toggle("Use Camera Instead")

if use_camera:
    image_file = st.camera_input("Take a photo")
else:
    image_file = st.file_uploader(
        "Upload CNIC image (Gallery)", 
        type=["jpg", "jpeg", "png"]
    )


# # File uploader (camera/gallery on mobile)
# image_file = st.file_uploader(
#     "Upload CNIC Image (Camera or Gallery)", 
#     type=["jpg", "jpeg", "png"], 
#     accept_multiple_files=False
# )

if image_file:
    image = Image.open(image_file)
    st.image(image, caption="Uploaded CNIC", use_column_width=True)

    # Convert image to base64
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode()

    # Prompt to extract CNIC fields
    prompt = """
    Extract the following fields from this Pakistani CNIC image:
    - Full Name
    - Father's Name
    - Gender
    - Nationality
    - Date of Birth
    - CNIC Number

    Respond only in this format:
    Name: ...
    Father's Name: ...
    Gender: ...
    Nationality: ...
    Date of Birth: ...
    CNIC Number: ...
    """

    # Call OpenAI GPT-4o with image
    with st.spinner("Extracting information using AI..."):
        try:
            response = openai.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that extracts text data from Pakistani CNIC images."},
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": prompt},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/png;base64,{img_base64}"
                                }
                            }
                        ],
                    }
                ],
                max_tokens=500
            )

            result_text = response.choices[0].message.content
            st.success("CNIC data extracted successfully!")
            st.text_area("Extracted Information:", result_text, height=220)

        except openai.OpenAIError as e:
            st.error(f"OpenAI API error: {e}")
