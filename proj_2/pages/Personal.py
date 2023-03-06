import streamlit as st
from matplotlib import image
import os

st.title("Personal -:blue[Guna info]")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")



# DATA_PATH = os.path.join(dir_of_interest, "data", "titanic.csv")
CODE = """ 
    I'm 
    Gunal K s/o kumar & kandharubi from Kallakuruchi.
    I'm comfortable 4 languages(English , tamil , kannada and Hindi)
    My Hobbies are Playing Volleyball , listening stories and
    visualing random plots
    Thanks for your time and Respect..
    Family lover and Brother lub
    Blue hearted with peace minded
    Insta Id  : crazy_killer1112"""

st.snow()
st.code(CODE , language ='python')
btn_click = st.button("Click here if like personal blog !")
IMAGE_PATH = os.path.join(dir_of_interest, "images", "blue.jpeg")

img = image.imread(IMAGE_PATH)
st.image(img)





if btn_click == True:
    st.subheader("You :thumbsup: Guna:heartbeat:")
    st.balloons()
