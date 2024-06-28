import streamlit as st
from langchain_helper import get_image_data

st.title("Google Lense 🖼️")

image_url = st.text_input("Enter image URL...")

if image_url:
    try:
        image_data = get_image_data(image_url)
        st.write("Image details:")
        st.write(f"Google Lens: {image_data}")
    except Exception as e:
        st.error(f"Error fetching image: {e}")
else:
    st.write("Please enter an image URL.")
