import requests
import streamlit as st
import os 

API_TOKEN = os.environ.get("API_TOKEN")
API_URL = os.environ.get("API_URL")


headers = {"Authorization": f"Bearer {API_TOKEN}"}

# Set the title and description of the app
st.title("Alzheimer's Detection")

# Create a file upload widget
uploaded_image = st.file_uploader("Upload an MRI", type=["jpg", "png", "jpeg"])

# if uploaded_image is not None:
#     # Display the uploaded image
#     st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

#     resp = requests.post(API_URL, headers=headers, data=uploaded_image)
#     result = resp.json()[0]
#     st.write(f"Label: {result['label']}")
#     st.write(f"Score: {result['score']}")

if uploaded_image is not None:
    col1, col2 = st.columns(2)

    with col1:
        st.write("#### Uploaded MRI")
        st.image(uploaded_image, caption="Uploaded MRI", use_column_width=True)

    with col2:
        resp = requests.post(API_URL, headers=headers, data=uploaded_image)
        result = resp.json()[0]
        st.write("#### Result")
        st.write(f"Label: {result['label']}")
        st.write(f"Score: {result['score']}")

