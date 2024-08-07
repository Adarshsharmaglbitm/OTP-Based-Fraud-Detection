import streamlit as st
import time
from geopy.geocoders import Nominatim
import math
import twilio
import random
from twilio.rest import Client



st.set_page_config(layout="wide")
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)





col1, col2 = st.columns(2)



with col1:
    st.image("https://m.media-amazon.com/images/I/71H0vxwB3PL._SX569_.jpg")

with col2:
    #st.image("https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/mba15-spacegray-config-202306?wid=840&hei=508&fmt=jpeg&qlt=90&.v=1684340991372")
    st.header("ASUS ROG Strix G15, AMD Ryzen 7 6800H, 15.6 (39.62 cm) FHD 144Hz, 4GB RTX 3050 Graphics, Gaming Laptop (16GB/1TB SSD/Windows 11/Gray/2.1 kg), G513RC-HN083W")
    st.header("PRICE::$1621")
    st.image("rating.png")
    st.page_link("pages/buynow.py", label="BUY NOW")



col3, col4 = st.columns(2)
with col3:
    st.image("https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcSK-rXVi9XkRVSb6K36Y3he6hEveRo8GnSak-wmXq27Q2QA47S27BTHmoLOWCpNJ-4S_qOV0g1AepRI1ADjAktKqZhz43iG_-1P1VCSdrR9QHy946aNM62p")


with col4:
    st.header("ASUS TUF Gaming F15, 15.6(39.62 cms) FHD 144Hz, Intel Core i7-11800H 11th Gen, 4GB NVIDIA GeForce RTX 3050 Ti, Gaming Laptop (16GB/512GB SSD/Windows 11/90WHrs Battery/Black/2.30 Kg), FX506HE-HN382W")
    st.header("PRICE::$1368")
    st.image("rating.png")
    st.page_link("pages/buynow.py", label="BUY NOW")

col5, col6 = st.columns(2)
with col5:
    st.image("https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcSK-rXVi9XkRVSb6K36Y3he6hEveRo8GnSak-wmXq27Q2QA47S27BTHmoLOWCpNJ-4S_qOV0g1AepRI1ADjAktKqZhz43iG_-1P1VCSdrR9QHy946aNM62p")


with col6:
    st.header("ASUS TUF Gaming F15, 15.6(39.62 cms) FHD 144Hz, Intel Core i7-11800H 11th Gen, 4GB NVIDIA GeForce RTX 3050 Ti, Gaming Laptop (16GB/512GB SSD/Windows 11/90WHrs Battery/Black/2.30 Kg), FX506HE-HN382W")
    st.header("PRICE::$1368")
    st.image("rating.png")
    st.page_link("pages/buynow.py", label="BUY NOW")

col7, col8 = st.columns(2)
with col7:
    st.image("https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcSK-rXVi9XkRVSb6K36Y3he6hEveRo8GnSak-wmXq27Q2QA47S27BTHmoLOWCpNJ-4S_qOV0g1AepRI1ADjAktKqZhz43iG_-1P1VCSdrR9QHy946aNM62p")


with col8:
    st.header("ASUS TUF Gaming F15, 15.6(39.62 cms) FHD 144Hz, Intel Core i7-11800H 11th Gen, 4GB NVIDIA GeForce RTX 3050 Ti, Gaming Laptop (16GB/512GB SSD/Windows 11/90WHrs Battery/Black/2.30 Kg), FX506HE-HN382W")
    st.header("PRICE::$1368")
    st.image("rating.png")
    st.page_link("pages/buynow.py", label="BUY NOW")

(col9, col10) = st.columns(2)
with col9:
    st.image("https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcSK-rXVi9XkRVSb6K36Y3he6hEveRo8GnSak-wmXq27Q2QA47S27BTHmoLOWCpNJ-4S_qOV0g1AepRI1ADjAktKqZhz43iG_-1P1VCSdrR9QHy946aNM62p")

with col10:
    st.header("ASUS TUF Gaming F15, 15.6(39.62 cms) FHD 144Hz, Intel Core i7-11800H 11th Gen, 4GB NVIDIA GeForce RTX 3050 Ti, Gaming Laptop (16GB/512GB SSD/Windows 11/90WHrs Battery/Black/2.30 Kg), FX506HE-HN382W")
    st.header("PRICE::$1368")
    st.image("rating.png")
    st.page_link("pages/buynow.py", label="BUY NOW")

col11, col12 = st.columns(2)
with col11:
    st.image("https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcSK-rXVi9XkRVSb6K36Y3he6hEveRo8GnSak-wmXq27Q2QA47S27BTHmoLOWCpNJ-4S_qOV0g1AepRI1ADjAktKqZhz43iG_-1P1VCSdrR9QHy946aNM62p")


with col12:
    st.header("ASUS TUF Gaming F15, 15.6(39.62 cms) FHD 144Hz, Intel Core i7-11800H 11th Gen, 4GB NVIDIA GeForce RTX 3050 Ti, Gaming Laptop (16GB/512GB SSD/Windows 11/90WHrs Battery/Black/2.30 Kg), FX506HE-HN382W")
    st.header("PRICE::$1368")
    st.image("rating.png")
    st.page_link("pages/buynow.py", label="BUY NOW")

col13, col14 = st.columns(2)
with col13:
    st.image("https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcSK-rXVi9XkRVSb6K36Y3he6hEveRo8GnSak-wmXq27Q2QA47S27BTHmoLOWCpNJ-4S_qOV0g1AepRI1ADjAktKqZhz43iG_-1P1VCSdrR9QHy946aNM62p")


with col14:
    st.header("ASUS TUF Ga` ming F15, 15.6(39.62 cms) FHD 144Hz, Intel Core i7-11800H 11th Gen, 4GB NVIDIA GeForce RTX 3050 Ti, Gaming Laptop (16GB/512GB SSD/Windows 11/90WHrs Battery/Black/2.30 Kg), FX506HE-HN382W")
    st.header("PRICE::$1368")
    st.image("rating.png")
    st.page_link("pages/buynow.py", label="BUY NOW")

