import streamlit as st
import pandas as pd
import subprocess
from PIL import Image
import base64

new_title = '<p style="font-family:times new roman; color:red; font-size: 42px;">IMAGE  CLASSIFICATION</p>'
st.markdown(new_title, unsafe_allow_html=True)



# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
# DB Management
import sqlite3 
conn = sqlite3.connect('data.db')
c = conn.cursor()
# DB  Functions
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data


global img
#def main():

img = Image.open("img2.jpg")


st.sidebar.title("Menu")

menu = ["Home","Login","SignUp"]

choice = st.sidebar.selectbox("Select",menu,key='1')
 

if choice == "Home":
    #st.subheader("Home")
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
    new_title1 = '<p style="font-family:times new roman; color:#FFD700; font-size: 30px;">About Application</p>'
    st.markdown(new_title1, unsafe_allow_html=True)
    st.markdown(" In this application, we use only six samples. The samples are our colleagues, this application helps to predict the each name of the colleagues. Image classification refers to the task of extracting information classes from a multiband raster image. The resulting raster from image classification can be used to create thematic maps. ")
    st.image(img,width = 800)
   
    
    
elif choice == "Login":
    main_bg = "img4.jpg"
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
    st.subheader("Login Section")
   
    username = st.text_input("User Name")
    password = st.text_input("Password",type='password')
    
    if st.button("Login"):
        # if password == '12345':
        create_usertable()
        hashed_pswd = make_hashes(password)

        result = login_user(username,check_hashes(password,hashed_pswd))
        if result:

            st.success("Logged In as {}".format(username))

            st.write("Image Classification app opens in new tab please wait")
            
            subprocess.Popen(["streamlit", "run", "Attendence.py"])


        else:
            st.warning("Incorrect Username/Password")





elif choice == "SignUp":

    main_bg = "img3.jpg"
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
    st.subheader("Login Section")
    
    st.subheader("Create New Account")
    new_user = st.text_input("Username")
    new_password = st.text_input("Create Password",type='password')
    #confirm_password = st.text_input("Confirm Password",type='password')

    if st.button("Signup"):
        create_usertable()
        add_userdata(new_user,make_hashes(new_password))
        st.success("You have successfully created a valid Account")
        st.info("Go to Login Menu to login")



# if __name__ == '__main__':
	# main()
    
