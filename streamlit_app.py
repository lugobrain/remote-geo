import streamlit as st
import image_cropper
import point_cloud_filter

st.title("Geospatial Processing Hub")

task = st.selectbox("Choose a task", ["Image Cropping", "Point Cloud Filtering"])

if task == "Image Cropping":
    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png"])
    if uploaded_file:
        result = image_cropper.run(uploaded_file)
        st.image(result)
        st.download_button("Download Cropped Image", result, "cropped.png")

elif task == "Point Cloud Filtering":
    uploaded_file = st.file_uploader("Upload Point Cloud", type=["las", "laz"])
    if uploaded_file:
        result = point_cloud_filter.run(uploaded_file)
        st.write("Filtered Point Cloud Preview")
        st.download_button("Download Filtered File", result, "filtered.las")
