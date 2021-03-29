import os
import json
import pandas as pd 
import streamlit as st 
import datetime
import random
import matplotlib.pyplot as plt 

st.write("# Parking Lot")

spots = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def information():
    f = open("data.txt", "a")
    f.write("\n" + spotstring)

def read_info():
    global spots
    f = open("data.txt", "r")
    for line in f:
        pass
    last_line = line
    newspots = last_line.rstrip().split(',')
    spots[0] = newspots[0]
    spots[1] = newspots[1]
    spots[2] = newspots[2]
    spots[3] = newspots[3]
    spots[4] = newspots[4]
    spots[5] = newspots[5]
    spots[6] = newspots[6]
    spots[7] = newspots[7]
    spots[8] = newspots[8]
    spots[9] = newspots[9]

spot_number = st.number_input("spot number (1-10)")
if st.button("reserve"):
    x = int(spot_number)
    if x == 1:
        read_info()
        if "0" in spots[0]:
            st.write("you have successfully reserved spot 1")
            spots[0] = 1
            spotstring = str(spots)
            information()
        else:
            st.write("that spot is already taken")
    if x == 2:
        read_info()
        if "0" in spots[1]:
            st.write("you have successfully reserved spot 2")
            spots[1] = 1
            spotstring = str(spots)
            information()
        else:
            st.write("that spot is already taken")
    if x == 3:
        read_info()
        if "0" in spots[2]:
            st.write("you have successfully reserved spot 3")
            spots[2] = 1
            spotstring = str(spots)
            information()
        else:
            st.write("that spot is already taken")
    if x == 4:
        read_info()
        if "0" in spots[3]:
            st.write("you have successfully reserved spot 4")
            spots[3] = 1
            spotstring = str(spots)
            information()
        else:
            st.write("that spot is already taken")
    if x == 5:
        read_info()
        if "0" in spots[4]:
            st.write("you have successfully reserved spot 5")
            spots[4] = 1
            spotstring = str(spots)
            information()
        else:
            st.write("that spot is already taken")
    if x == 6:
        read_info()
        if "0" in spots[5]:
            st.write("you have successfully reserved spot 6")
            spots[5] = 1
            spotstring = str(spots)
            information()
        else:
            st.write("that spot is already taken")
    if x == 7:
        read_info()
        if "0" in spots[6]:
            st.write("you have successfully reserved spot 7")
            spots[6] = 1
            spotstring = str(spots)
            information()
        else:
            st.write("that spot is already taken")
    if x == 8:
        read_info()
        if "0" in spots[7]:
            st.write("you have successfully reserved spot 8")
            spots[7] = 1
            spotstring = str(spots)
            information()
        else:
            st.write("that spot is already taken")
    if x == 9:
        read_info()
        if "0" in spots[8]:
            st.write("you have successfully reserved spot 9")
            spots[8] = 1
            spotstring = str(spots)
            information()
        else:
            st.write("that spot is already taken")
    if x == 10:
        read_info()
        if "0" in spots[9]:
            st.write("you have successfully reserved spot 10")
            spots[9] = 1
            spotstring = str(spots)
            information()
        else:
            st.write("that spot is already taken")

free_spot = st.number_input("parking spot number (1-10)")
if st.button("free"):
    y = int(free_spot)
    if y == 1:
        read_info()
        if "0" not in spots[0]:
            st.write("you have freed spot 1")
            spots[0] = 0
            spotstring = str(spots)
            information()
        else:
            st.write("that spot has not been reserved")
    if y == 2:
        read_info()
        if "0" not in spots[1]:
            st.write("you have freed spot 2")
            spots[1] = 0
            spotstring = str(spots)
            information()
        else:
            st.write("that spot has not been reserved")
    if y == 3:
        read_info()
        if "0" not in spots[2]:
            st.write("you have freed spot 3")
            spots[2] = 0
            spotstring = str(spots)
            information()
        else:
            st.write("that spot has not been reserved")
    if y == 4:
        read_info()
        if "0" not in spots[3]:
            st.write("you have freed spot 4")
            spots[3] = 0
            spotstring = str(spots)
            information()
        else:
            st.write("that spot has not been reserved")
    if y == 5:
        read_info()
        if "0" not in spots[4]:
            st.write("you have freed spot 5")
            spots[4] = 0
            spotstring = str(spots)
            information()
        else:
            st.write("that spot has not been reserved")
    if y == 6:
        read_info()
        if "0" not in spots[5]:
            st.write("you have freed spot 6")
            spots[5] = 0
            spotstring = str(spots)
            information()
        else:
            st.write("that spot has not been reserved")
    if y == 7:
        read_info()
        if "0" not in spots[6]:
            st.write("you have freed spot 7")
            spots[6] = 0
            spotstring = str(spots)
            information()
        else:
            st.write("that spot has not been reserved")
    if y == 8:
        read_info()
        if "0" not in spots[7]:
            st.write("you have freed spot 8")
            spots[7] = 0
            spotstring = str(spots)
            information()
        else:
            st.write("that spot has not been reserved")
    if y == 9:
        read_info()
        if "0" not in spots[8]:
            st.write("you have freed spot 9")
            spots[8] = 0
            spotstring = str(spots)
            information()
        else:
            st.write("that spot has not been reserved")
    if y == 10:
        read_info()
        if "0" not in spots[9]:
            st.write("you have freed spot 10")
            spots[9] = 0
            spotstring = str(spots)
            information()
        else:
            st.write("that spot has not been reserved")

if st.button("view available spots"):
    read_info()
    freespots = ""
    if "0" in spots[0]:
        freespots = freespots + "1, "
    if "0" in spots[1]:
        freespots = freespots + "2, "
    if "0" in spots[2]:
        freespots = freespots + "3, "
    if "0" in spots[3]:
        freespots = freespots + "4, "
    if "0" in spots[4]:
        freespots = freespots + "5, "
    if "0" in spots[5]:
        freespots = freespots + "6, "
    if "0" in spots[6]:
        freespots = freespots + "7, "
    if "0" in spots[7]:
        freespots = freespots + "8, "
    if "0" in spots[8]:
        freespots = freespots + "9, "
    if "0" in spots[9]:
        freespots = freespots + "10"
    st.write(freespots)
