from PIL import Image
import io

def run(uploaded_file, crop_size=(200, 200)):
    image = Image.open(uploaded_file)
    width, height = image.size

    # Calculate cropping box
    left = (width - crop_size[0]) / 2
    top = (height - crop_size[1]) / 2
    right = (width + crop_size[0]) / 2
    bottom = (height + crop_size[1]) / 2

    cropped_image = image.crop((left, top, right, bottom))

    # Save to buffer for Streamlit download
    buf = io.BytesIO()
    cropped_image.save(buf, format="PNG")
    buf.seek(0)
    return buf
