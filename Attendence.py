import streamlit as st
#from img_classification import teachable_machine_classification
from PIL import Image, ImageOps
#import playsound
import base64
import subprocess

new_main_title = '<p style="font-family:times new roman; color:red; font-size: 42px;">COMPUTER VISION</p>'
st.markdown(new_main_title, unsafe_allow_html=True)

st.write(' In this application we can do image classification,basic image processing,advanced image processing and face detection. Now we are going to see what is these and how this app works for these individually are given below. If you know about those things you can give "Get Started" for the application.')
if st.button("Get Started"):
    subprocess.Popen(["streamlit", "run", "final.py"])
    
    
new_title = '<p style="font-family:times new roman; color:red; font-size: 35px;">Image Classification</p>'
st.markdown(new_title, unsafe_allow_html=True)

# home = st.sidebar.radio(
    # label="Select",
    # options=['General', 'App'])
main_bg = "bd1.jpg"
main_bg_ext = "jpg"


st.write(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# if home == 'General':


st.write("Image classification refers to the task of extracting information classes from a multiband raster image. The resulting raster from image classification can be used to create thematic maps. Depending on the interaction between the analyst and the computer during classification. ")

img = Image.open("img1.png")
st.image(img,width = 600)


new_title1 = '<p style="font-family:Comic Sans MS; color:#0e7e0d; font-size: 25px;">Steps for Image Classification</p>'
st.markdown(new_title1, unsafe_allow_html=True)
st.write("Before going to the app we must follow some steps to classify the image. Those steps are given below.")

new_title3 = '<p style="font-family:Comic Sans MS; color:#0e7e0d; font-size: 18px;">Step 1</p>'
st.markdown(new_title3, unsafe_allow_html=True)
st.write("Browse the image from the local disk by clicking the browse files.")

new_title4 = '<p style="font-family:Comic Sans MS; color:#0e7e0d; font-size: 18px;">Step 2</p>'
st.markdown(new_title4, unsafe_allow_html=True)
st.write("After selecting the image the app predict the person in the image.")

new_title5 = '<p style="font-family:Comic Sans MS; color:#0e7e0d; font-size: 18px;">Step 3</p>'
st.markdown(new_title5, unsafe_allow_html=True)
st.write("The app tells us who is in the image after the prediction.")



new_title = '<p style="font-family:times new roman; color:red; font-size: 35px;">Basic Image Processing</p>'
st.markdown(new_title, unsafe_allow_html=True)
st.write('In this "Basic Image Processing" you can do Grayscale,Resizing the image,Rotating the image,Cropping the image.')


new_title6 = '<p style="font-family:Comic Sans MS; color:red; font-size: 25px;">Grayscale</p>'
st.markdown(new_title6, unsafe_allow_html=True)
st.write("In digital images, grayscale means that the value of each pixel represents only the intensity information of the light. Such images typically display only the darkest black to the brightest white. In other words, the image contains only black, white, and gray colors, in which gray has multiple levels.")

new_title7 = '<p style="font-family:Comic Sans MS; color:#0e7e0d; font-size: 18px;">Steps for Grayscale</p>'
st.markdown(new_title7, unsafe_allow_html=True)   
st.write("Browse the image from the local disk by clicking the browse files. If you gave the input image then the grayscale for that image will come automatically.")
  
  
new_title8 = '<p style="font-family:Comic Sans MS; color:red; font-size: 25px;">Resize</p>'
st.markdown(new_title8, unsafe_allow_html=True)
st.write('When an image is resized, its pixel information is changed. For example, an image is reduced in size, any unneeded pixel information will be discarded by the photo editor')

new_title9 = '<p style="font-family:Comic Sans MS; color:#0e7e0d; font-size: 18px;">Steps for Resize</p>'
st.markdown(new_title9, unsafe_allow_html=True)
new_title10 = '<p style="font-family:Comic Sans MS; color:#0e7e0d; font-size: 18px;">Step 1</p>'
st.markdown(new_title10, unsafe_allow_html=True)
st.write("Browse the image from the local disk by clicking the browse files.")

new_title11 = '<p style="font-family:Comic Sans MS; color:#0e7e0d; font-size: 18px;">Step 2</p>'
st.markdown(new_title11, unsafe_allow_html=True)
st.write("Select the height from the sidebar which ranges between 0 to 1000.")

new_title12 = '<p style="font-family:Comic Sans MS; color:#0e7e0d; font-size: 18px;">Step 3</p>'
st.markdown(new_title12, unsafe_allow_html=True)
st.write("Select the width from the sidebar which is also ranges between 0 to 1000.")

new_title12 = '<p style="font-family:Comic Sans MS; color:#0e7e0d; font-size: 18px;">Step 4</p>'
st.markdown(new_title12, unsafe_allow_html=True)
st.write("After selecting the height and width you can see the result of the image.")


new_title13 = '<p style="font-family:Comic Sans MS; color:red; font-size: 25px;">Rotate</p>'
st.markdown(new_title13, unsafe_allow_html=True)
st.write("When referring to an image or image editor, rotate is a feature that allows you to turn an image in a clockwise or counterclockwise direction.")

new_title14 = '<p style="font-family:Comic Sans MS; color:#0e7e0d; font-size: 18px;">Steps for Rotate</p>'
st.markdown(new_title14, unsafe_allow_html=True)
st.write("Browse the image from the local disk by clicking the browse files. The you can rotate the image by changing their degree which given in the sidebar.")


new_title15 = '<p style="font-family:Comic Sans MS; color:red; font-size: 25px;">Croping</p>'
st.markdown(new_title15, unsafe_allow_html=True)
st.write(" Cropping is the removal of unwanted outer areas from a photographic or illustrated image. The process usually consists of the removal of some of the peripheral areas of an image to remove extraneous trash from the picture, to improve its framing, to change the aspect ratio, or to accentuate or isolate the subject matter from its background.")

new_title16 = '<p style="font-family:Comic Sans MS; color:#0e7e0d; font-size: 18px;">Steps for Cropping</p>'
st.markdown(new_title16, unsafe_allow_html=True)
new_title16 = '<p style="font-family:Comic Sans MS; color:#0e7e0d; font-size: 18px;">Step 1</p>'
st.markdown(new_title16, unsafe_allow_html=True)
st.write("Browse the image from the local disk by clicking the browse files.")

new_title17 = '<p style="font-family:Comic Sans MS; color:#0e7e0d; font-size: 18px;">Step 2</p>'
st.markdown(new_title17, unsafe_allow_html=True)
st.write("You can adjust the height from top to bottom and bottom to top in the sidebar.")

new_title18 = '<p style="font-family:Comic Sans MS; color:#0e7e0d; font-size: 18px;">Step 3</p>'
st.markdown(new_title18, unsafe_allow_html=True)
st.write("You can adjust the width from left to right and right to left in the sidebar.")

new_title19 = '<p style="font-family:Comic Sans MS; color:#0e7e0d; font-size: 18px;">Step 4</p>'
st.markdown(new_title19, unsafe_allow_html=True)
st.write("After selecting the height and width you can see the result of the image.")



new_title20 = '<p style="font-family:times new roman; color:red; font-size: 35px;">Advanced Image Processing</p>'
st.markdown(new_title20, unsafe_allow_html=True)
st.write('In this "Advanced Image Processing" you can alter the threshold of the image and find the edges in the image and also you can see the sobel edges')


new_title21 = '<p style="font-family:Comic Sans MS; color:red; font-size: 25px;">Threshold</p>'
st.markdown(new_title21, unsafe_allow_html=True)
st.write("Threshold is to change the pixels of an image to make the image easier to analyze. In thresholding, we convert an image from color or grayscale into a binary image, i.e., one that is simply black and white. Most frequently, we use thresholding as a way to select areas of interest of an image, while ignoring the parts we are not concerned with. ")

new_title22 = '<p style="font-family:Comic Sans MS; color:#0e7e0d; font-size: 18px;">Steps for Threshold</p>'
st.markdown(new_title22, unsafe_allow_html=True)
new_title23 = '<p style="font-family:Comic Sans MS; color:#0e7e0d; font-size: 18px;">Step 1</p>'
st.markdown(new_title23, unsafe_allow_html=True)
st.write("Browse the image from the local disk by clicking the browse files.")

new_title24 = '<p style="font-family:Comic Sans MS; color:#0e7e0d; font-size: 18px;">Step 2</p>'
st.markdown(new_title24, unsafe_allow_html=True)
st.write("You can see the threshold of the image.")

new_title25 = '<p style="font-family:Comic Sans MS; color:#0e7e0d; font-size: 18px;">Step 3</p>'
st.markdown(new_title25, unsafe_allow_html=True)
st.write("If you change the threshold value through the slider then the image get altered.")

new_title26 = '<p style="font-family:Comic Sans MS; color:#0e7e0d; font-size: 18px;">Step 4</p>'
st.markdown(new_title26, unsafe_allow_html=True)
st.write("After that you can also see the histogram which is plotted with respect to the threshold image.")


new_title27 = '<p style="font-family:Comic Sans MS; color:red; font-size: 25px;">Edge Detection</p>'
st.markdown(new_title27, unsafe_allow_html=True)
st.write("Edge detection is a technique of image processing used to identify points in a digital image with discontinuities, simply to say, sharp changes in the image brightness. These points where the image brightness varies sharply are called the edges. ")

new_title28 = '<p style="font-family:Comic Sans MS; color:#0e7e0d; font-size: 18px;">Steps for Edge Detection</p>'
st.markdown(new_title28, unsafe_allow_html=True)
new_title29 = '<p style="font-family:Comic Sans MS; color:#0e7e0d; font-size: 18px;">Step 1</p>'
st.markdown(new_title29, unsafe_allow_html=True)
st.write("Browse the image from the local disk by clicking the browse files.")

new_title30 = '<p style="font-family:Comic Sans MS; color:#0e7e0d; font-size: 18px;">Step 2</p>'
st.markdown(new_title30, unsafe_allow_html=True)
st.write("Atter choosing the image then the edges of the image is shown.")

new_title31 = '<p style="font-family:Comic Sans MS; color:#0e7e0d; font-size: 18px;">Step 3</p>'
st.markdown(new_title31, unsafe_allow_html=True)
st.write("By changing the threshold value in the sidebar you can change the edges in the image.")



new_title32 = '<p style="font-family:times new roman; color:red; font-size: 35px;">Face Detection</p>'
st.markdown(new_title32, unsafe_allow_html=True)
st.write("Face detection also called facial detection is an artificial intelligence (AI) based computer technology used to find and identify human faces in digital images. It now plays an important role as the first step in many key applications including face tracking, face analysis and facial recognition.")

new_title33 = '<p style="font-family:Comic Sans MS; color:#0e7e0d; font-size: 18px;">Steps for Face Detection</p>'
st.markdown(new_title33, unsafe_allow_html=True)
st.write("After giving the input image the output image will be shown as the face is highlighted by the rectangle.")