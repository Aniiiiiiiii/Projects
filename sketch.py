# -*- coding: utf-8 -*-
"""Sketch.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17T2dcCUCLh3gPFjbpN7-r4epKtkVHLL5
"""

pip install streamlit pillow numpy opencv-python-headless

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# PAGE_CONFIG = {"page_title":"StColab.io","page_icon":":smiley:","layout":"centered"}
# st.beta_set_page_config(**PAGE_CONFIG)
# 
# 
# def main():
# 	st.title("Awesome Streamlit for ML")
# 	st.subheader("How to run streamlit from colab")
# 
# 
# 	menu = ["Home","About"]
# 	choice = st.sidebar.selectbox('Menu',menu)
# 	if choice == 'Home':
# 		st.subheader("Streamlit From Colab")
# 
# 
# 
# if __name__ == '__main__':
# 	main()

!pip install pyngrok==4.1.1

from pyngrok import ngrok
public_url = ngrok.connect(port='80')
print (public_url)
!streamlit run app.py >/dev/null

from pyngrok import ngrok
public_url = ngrok.connect(port='80')

# Import necessary libraries
import streamlit as st
from PIL import Image
import numpy as np
import cv2

# Define functions for sketch conversion
def convert_to_pencil_sketch(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_image = 255 - gray_image
    blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), sigmaX=0, sigmaY=0)
    inverted_blurred_image = 255 - blurred_image
    pencil_sketch = cv2.divide(255 - gray_image, inverted_blurred_image, scale=256.0)
    return pencil_sketch

def main():
    st.title('Image to Pencil Sketch Converter')
    st.write("Upload an image and convert it to a pencil sketch.")

    # Upload image through Streamlit file uploader
    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_image is not None:
        # Load the image
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Convert the image to a NumPy array
        image_np = np.array(image)

        # Convert to pencil sketch
        sketch = convert_to_pencil_sketch(image_np)

        # Display the sketch
        st.image(sketch, caption="Pencil Sketch", use_column_width=True)

if __name__ == '__main__':
    main()

!streamlit run /usr/local/lib/python3.10/dist-packages/ipykernel_launcher.py

# import the frameworks, packages and libraries
import streamlit as st
from PIL import Image
from io import BytesIO
import numpy as np
import cv2 # computer vision

# function to convert an image to a
# water color sketch
def convertto_watercolorsketch(inp_img):
	img_1 = cv2.edgePreservingFilter(inp_img, flags=2, sigma_s=50, sigma_r=0.8)
	img_water_color = cv2.stylization(img_1, sigma_s=100, sigma_r=0.5)
	return(img_water_color)

# function to convert an image to a pencil sketch
def pencilsketch(inp_img):
	img_pencil_sketch, pencil_color_sketch = cv2.pencilSketch(
		inp_img, sigma_s=50, sigma_r=0.07, shade_factor=0.0825)
	return(img_pencil_sketch)

# function to load an image
def load_an_image(image):
	img = Image.open(image)
	return img

# the main function which has the code for
# the web application
def main():

	# basic heading and titles
	st.title('WEB APPLICATION TO CONVERT IMAGE TO SKETCH')
	st.write("This is an application developed for converting\
	your ***image*** to a ***Water Color Sketch*** OR ***Pencil Sketch***")
	st.subheader("Please Upload your image")

	# image file uploader
	image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"])

	# if the image is uploaded then execute these
	# lines of code
	if image_file is not None:

		# select box (drop down to choose between water
		# color / pencil sketch)
		option = st.selectbox('How would you like to convert the image',
							('Convert to water color sketch',
							'Convert to pencil sketch'))
		if option == 'Convert to water color sketch':
			image = Image.open(image_file)
			final_sketch = convertto_watercolorsketch(np.array(image))
			im_pil = Image.fromarray(final_sketch)

			# two columns to display the original image and the
			# image after applying water color sketching effect
			col1, col2 = st.columns(2)
			with col1:
				st.header("Original Image")
				st.image(load_an_image(image_file), width=250)

			with col2:
				st.header("Water Color Sketch")
				st.image(im_pil, width=250)
				buf = BytesIO()
				img = im_pil
				img.save(buf, format="JPEG")
				byte_im = buf.getvalue()
				st.download_button(
					label="Download image",
					data=byte_im,
					file_name="watercolorsketch.png",
					mime="image/png"
				)

		if option == 'Convert to pencil sketch':
			image = Image.open(image_file)
			final_sketch = pencilsketch(np.array(image))
			im_pil = Image.fromarray(final_sketch)

			# two columns to display the original image
			# and the image after applying
			# pencil sketching effect
			col1, col2 = st.columns(2)
			with col1:
				st.header("Original Image")
				st.image(load_an_image(image_file), width=250)

			with col2:
				st.header("Pencil Sketch")
				st.image(im_pil, width=250)
				buf = BytesIO()
				img = im_pil
				img.save(buf, format="JPEG")
				byte_im = buf.getvalue()
				st.download_button(
					label="Download image",
					data=byte_im,
					file_name="watercolorsketch.png",
					mime="image/png"
				)


if __name__ == '__main__':
	main()

!pip install ipywidgets

import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, HTML, clear_output
import ipywidgets as widgets
from IPython.display import display as display_widget

# function to convert an image to a pencil sketch
def pencilsketch(inp_img, sigma_s=50, sigma_r=0.07):
    img_pencil_sketch, _ = cv2.pencilSketch(
        inp_img, sigma_s=sigma_s, sigma_r=sigma_r, shade_factor=0.0825)
    return img_pencil_sketch

# function to convert an image to a watercolor sketch
def watercolorsketch(inp_img, sigma_s=100, sigma_r=0.5):
    img_1 = cv2.edgePreservingFilter(inp_img, flags=2, sigma_s=sigma_s, sigma_r=0.8)
    img_water_color = cv2.stylization(img_1, sigma_s=sigma_s, sigma_r=sigma_r)
    return img_water_color

# function to load an image
def load_an_image(image_path):
    img = cv2.imread(image_path)
    return img

# User Input Validation
def validate_image_format(image_path):
    valid_formats = ["png", "jpg", "jpeg"]
    image_format = image_path.split(".")[-1]
    return image_format.lower() in valid_formats

# Image Preprocessing
def preprocess_image(image, crop=False, resize=None, brightness=1.0, contrast=1.0):
    if crop:
        image = image[:resize, :resize]
    if resize:
        image = cv2.resize(image, (resize, resize))
    image = cv2.convertScaleAbs(image, alpha=brightness, beta=0)
    return cv2.convertScaleAbs(image, alpha=contrast, beta=0)

# Load your image
image_path = "/content/Donut.png"  # Replace with the path to your image

if validate_image_format(image_path):
    image = load_an_image(image_path)

    # Image Preprocessing
    image = preprocess_image(image, crop=False, resize=None, brightness=1.0, contrast=1.0)

    # Create subplots to display images
    fig, axes = plt.subplots(1, 3, figsize=(20, 5))

    # Display the original image
    axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axes[0].set_title("Original Image")
    axes[0].axis('off')

    # Pencil Sketch Customization
    sigma_s_pencil = 50
    sigma_r_pencil = 0.07

    # Slider for Sigma_s (Pencil Sketch)
    display(HTML("<h3>Sigma_s (Pencil Sketch):</h3>"))
    sigma_s_pencil_slider = widgets.IntSlider(value=sigma_s_pencil, min=1, max=100)
    display_widget(sigma_s_pencil_slider)
    clear_output(wait=True)
    sigma_s_pencil = sigma_s_pencil_slider.value

    # Slider for Sigma_r (Pencil Sketch)
    display(HTML("<h3>Sigma_r (Pencil Sketch):</h3>"))
    sigma_r_pencil_slider = widgets.FloatSlider(value=sigma_r_pencil, min=0.01, max=1.0, step=0.01)
    display_widget(sigma_r_pencil_slider)
    clear_output(wait=True)
    sigma_r_pencil = sigma_r_pencil_slider.value

    # Convert the image to a pencil sketch
    pencil_sketch = pencilsketch(image, sigma_s=sigma_s_pencil, sigma_r=sigma_r_pencil)

    # Display the Pencil Sketch
    axes[1].imshow(cv2.cvtColor(pencil_sketch, cv2.COLOR_BGR2RGB))
    axes[1].set_title("Pencil Sketch")
    axes[1].axis('off')

    # Watercolor Sketch Customization
    sigma_s_watercolor = 100
    sigma_r_watercolor = 0.5

    # Slider for Sigma_s (Watercolor Sketch)
    display(HTML("<h3>Sigma_s (Watercolor Sketch):</h3>"))
    sigma_s_watercolor_slider = widgets.IntSlider(value=sigma_s_watercolor, min=1, max=100)
    display_widget(sigma_s_watercolor_slider)
    clear_output(wait=True)
    sigma_s_watercolor = sigma_s_watercolor_slider.value

    # Slider for Sigma_r (Watercolor Sketch)
    display(HTML("<h3>Sigma_r (Watercolor Sketch):</h3>"))
    sigma_r_watercolor_slider = widgets.FloatSlider(value=sigma_r_watercolor, min=0.01, max=1.0, step=0.01)
    display_widget(sigma_r_watercolor_slider)
    clear_output(wait=True)
    sigma_r_watercolor = sigma_r_watercolor_slider.value

    # Convert the image to a watercolor sketch
    watercolor_sketch = watercolorsketch(image, sigma_s=sigma_s_watercolor, sigma_r=sigma_r_watercolor)

    # Display the Watercolor Sketch
    axes[2].imshow(cv2.cvtColor(watercolor_sketch, cv2.COLOR_BGR2RGB))
    axes[2].set_title("Watercolor Sketch")
    axes[2].axis('off')

    # Display all images
    plt.show()
else:
    print("Invalid image format. Supported formats: png, jpg, jpeg")

import cv2
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, HTML, clear_output
from IPython.display import display as display_widget

# Load your image
image_path = "/content/Donut.png"  # Updated image path

def validate_image_format(image_path):
    valid_formats = ["png", "jpg", "jpeg"]
    image_format = image_path.split(".")[-1]
    return image_format.lower() in valid_formats

def preprocess_image(image, crop=False, resize=None, brightness=1.0, contrast=1.0):
    if crop:
        image = image[:resize, :resize]
    if resize:
        image = cv2.resize(image, (resize, resize))
    image = cv2.convertScaleAbs(image, alpha=brightness, beta=0)
    return cv2.convertScaleAbs(image, alpha=contrast, beta=0)

def oil_painting_effect(image, size=7):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(image, 9, 300, 300)
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon

if validate_image_format(image_path):
    image = cv2.imread(image_path)

    # Image Preprocessing
    image = preprocess_image(image, crop=False, resize=None, brightness=1.0, contrast=1.0)

    # Create subplots to display images
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Display the original image
    axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axes[0].set_title("Original Image")
    axes[0].axis('off')

    # Oil Painting Effect Customization
    oil_painting_size = 7

    # Slider for Oil Painting Size
    display(HTML("<h3>Oil Painting Size:</h3>"))
    oil_painting_size_slider = widgets.IntSlider(value=oil_painting_size, min=1, max=15)
    display_widget(oil_painting_size_slider)
    clear_output(wait=True)
    oil_painting_size = oil_painting_size_slider.value

    # Apply the oil painting effect
    oil_painting_result = oil_painting_effect(image, size=oil_painting_size)

    # Display the Oil Painting Effect
    axes[1].imshow(cv2.cvtColor(oil_painting_result, cv2.COLOR_BGR2RGB))
    axes[1].set_title("Oil Painting Effect")
    axes[1].axis('off')

    plt.tight_layout()
    plt.show()
else:
    print("Invalid image format. Supported formats: png, jpg, jpeg")

import cv2
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, HTML, clear_output
from IPython.display import display as display_widget

# Load your image
image_path = "/content/Donut.png"  # Updated image path

def validate_image_format(image_path):
    valid_formats = ["png", "jpg", "jpeg"]
    image_format = image_path.split(".")[-1]
    return image_format.lower() in valid_formats

def preprocess_image(image, crop=False, resize=None, brightness=1.0, contrast=1.0):
    if crop:
        image = image[:resize, :resize]
    if resize:
        image = cv2.resize(image, (resize, resize))
    image = cv2.convertScaleAbs(image, alpha=brightness, beta=0)
    return cv2.convertScaleAbs(image, alpha=contrast, beta=0)

def cartoon_effect(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply a median blur to reduce noise and create a smoother appearance
    gray = cv2.medianBlur(gray, 5)

    # Detect edges in the image using adaptive thresholding
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # Create a color version of the image
    color = cv2.bilateralFilter(image, 9, 300, 300)

    # Combine the edges and color to create the cartoon effect
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon

if validate_image_format(image_path):
    image = cv2.imread(image_path)

    # Image Preprocessing
    image = preprocess_image(image, crop=False, resize=None, brightness=1.0, contrast=1.0)

    # Create subplots to display images
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Display the original image
    axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axes[0].set_title("Original Image")
    axes[0].axis('off')

    # Cartoon Effect
    cartoon_result = cartoon_effect(image)

    # Display the Cartoon Effect
    axes[1].imshow(cartoon_result, cmap='gray')
    axes[1].set_title("Cartoon Effect")
    axes[1].axis('off')

    plt.tight_layout()
    plt.show()
else:
    print("Invalid image format. Supported formats: png, jpg, jpeg")

import cv2
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, HTML, clear_output
from IPython.display import display as display_widget

# Load your image
image_path = "/content/Donut.png"  # Updated image path

def validate_image_format(image_path):
    valid_formats = ["png", "jpg", "jpeg"]
    image_format = image_path.split(".")[-1]
    return image_format.lower() in valid_formats

def preprocess_image(image, crop=False, resize=None, brightness=1.0, contrast=1.0):
    if crop:
        image = image[:resize, :resize]
    if resize:
        image = cv2.resize(image, (resize, resize))
    image = cv2.convertScaleAbs(image, alpha=brightness, beta=0)
    return cv2.convertScaleAbs(image, alpha=contrast, beta=0)

def apply_sepia_toning(image):
    # Define the sepia filter
    sepia_filter = np.array([[0.272, 0.534, 0.131],
                             [0.349, 0.686, 0.168],
                             [0.393, 0.769, 0.189]])

    # Apply the sepia filter to the image
    sepia_image = cv2.transform(image, sepia_filter)

    # Clip values to ensure they are within the valid range
    sepia_image = np.clip(sepia_image, 0, 255).astype(np.uint8)

    return sepia_image

if validate_image_format(image_path):
    image = cv2.imread(image_path)

    # Image Preprocessing
    image = preprocess_image(image, crop=False, resize=None, brightness=1.0, contrast=1.0)

    # Create subplots to display images
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Display the original image
    axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axes[0].set_title("Original Image")
    axes[0].axis('off')

    # Sepia Toning Effect
    sepia_result = apply_sepia_toning(image)

    # Display the Sepia Toning Effect
    axes[1].imshow(cv2.cvtColor(sepia_result, cv2.COLOR_BGR2RGB))
    axes[1].set_title("Sepia Toning Effect")
    axes[1].axis('off')

    plt.tight_layout()
    plt.show()
else:
    print("Invalid image format. Supported formats: png, jpg, jpeg")

import cv2
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, HTML, clear_output
from IPython.display import display as display_widget

# Load your image
image_path = "/content/Donut.png"  # Updated image path

def validate_image_format(image_path):
    valid_formats = ["png", "jpg", "jpeg"]
    image_format = image_path.split(".")[-1]
    return image_format.lower() in valid_formats

def preprocess_image(image, crop=False, resize=None, brightness=1.0, contrast=1.0):
    if crop:
        image = image[:resize, :resize]
    if resize:
        image = cv2.resize(image, (resize, resize))
    image = cv2.convertScaleAbs(image, alpha=brightness, beta=0)
    return cv2.convertScaleAbs(image, alpha=contrast, beta=0)

def apply_gaussian_blur(image, kernel_size=(5, 5)):
    return cv2.GaussianBlur(image, kernel_size, 0)

if validate_image_format(image_path):
    image = cv2.imread(image_path)

    # Image Preprocessing
    image = preprocess_image(image, crop=False, resize=None, brightness=1.0, contrast=1.0)

    # Create subplots to display images
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Display the original image
    axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axes[0].set_title("Original Image")
    axes[0].axis('off')

    # Gaussian Blur Effect
    gaussian_blur_result = apply_gaussian_blur(image, kernel_size=(15, 15))

    # Display the Gaussian Blur Effect
    axes[1].imshow(cv2.cvtColor(gaussian_blur_result, cv2.COLOR_BGR2RGB))
    axes[1].set_title("Gaussian Blur Effect")
    axes[1].axis('off')

    plt.tight_layout()
    plt.show()
else:
    print("Invalid image format. Supported formats: png, jpg, jpeg")

import cv2
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, HTML, clear_output
from IPython.display import display as display_widget

# Load your image
image_path = "/content/Donut.png"  # Updated image path

def validate_image_format(image_path):
    valid_formats = ["png", "jpg", "jpeg"]
    image_format = image_path.split(".")[-1]
    return image_format.lower() in valid_formats

def preprocess_image(image, crop=False, resize=None, brightness=1.0, contrast=1.0):
    if crop:
        image = image[:resize, :resize]
    if resize:
        image = cv2.resize(image, (resize, resize))
    image = cv2.convertScaleAbs(image, alpha=brightness, beta=0)
    return cv2.convertScaleAbs(image, alpha=contrast, beta=0)

def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

if validate_image_format(image_path):
    image = cv2.imread(image_path)

    # Image Preprocessing
    image = preprocess_image(image, crop=False, resize=None, brightness=1.0, contrast=1.0)

    # Create subplots to display images
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Display the original image
    axes[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axes[0].set_title("Original Image")
    axes[0].axis('off')

    # Grayscale Conversion
    grayscale_result = convert_to_grayscale(image)

    # Display the Grayscale Image
    axes[1].imshow(grayscale_result, cmap='gray')
    axes[1].set_title("Grayscale Image")
    axes[1].axis('off')

    plt.tight_layout()
    plt.show()
else:
    print("Invalid image format. Supported formats: png, jpg, jpeg")