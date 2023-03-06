import streamlit as st
from matplotlib import image
import os

st.title(" Professional info -:blue[Gunal K]")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")


# DATA_PATH = os.path.join(dir_of_interest, "data", "titanic.csv")

CODE = """ 
    I'm 
    I'm Gunal.K From Tamil Nadu .pursuing final year, 
     Bachelor of engineering (Computer science and engineering) 
     JCT college engineering and technology with CGPA(7.85 Till VI Sem), 
     Completed My primary schooling at Blossom school (Bangalore) 
     Higher secondary at Govt Higher secondary school (Rishivandhiyam ).
     I have knowledge in Python programming language ,
     Python libraries ,
     ML libraries
     Data analysis , 
     data visualization(Power BI . IBM Cognos), 
     Future Aim : data scientist ..
     
     Resume CV :https://drive.google.com/file/d/11IodcQpymt4SrNXEZbO3HrFv15JLGlnd/view?usp=share_link
     Mail : gunagunal142@gamail.com , gunagunal1112@gmail.com

     Linkden : Gunal K (www.linkedin.com/in/gunagunal1112)
     Github :  gunal11 (https://github.com/gunal11)
     Power bi works :https://drive.google.com/drive/folders/1GZR8-VIgURgBszB-vGfQP9mKqE8wi-6x?usp=share_link
     Works of colab : https://drive.google.com/drive/folders/1SrKSEUESyNyZzrmOCzcQPsnPI-3nf7K2?usp=share_link

     
     """

st.snow()     

st.code(CODE , language ='python')

btn_click = st.button("Click here if like professional blog !")
IMAGE_PATH = os.path.join(dir_of_interest, "images", "Coat.jpg")
img = image.imread(IMAGE_PATH)
st.image(img)

if btn_click == True:
    st.subheader("You :thumbsup: Gunal k professional info")
    st.balloons()