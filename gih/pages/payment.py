import streamlit as st
import math
import sqlite3

def distance(lat1, lon1, lat2, lon2):
    # Convert degrees to radians
    lon1 = lon1 * math.pi / 180
    lon2 = lon2 * math.pi / 180
    lat1 = lat1 * math.pi / 180
    lat2 = lat2 * math.pi / 180

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.pow(math.sin(dlat / 2), 2) + math.cos(lat1) * math.cos(lat2) * math.pow(math.sin(dlon / 2), 2)
    c = 2 * math.asin(math.sqrt(a))

    # Radius of earth in kilometers
    r = 6371

    # Calculate the result
    return c * r



# Set the page configuration
st.set_page_config(
    page_title="Payment Verification",
    page_icon="🔢",
    layout="centered",
    initial_sidebar_state="auto"
)

# Streamlit layout
st.markdown('<div class="container">', unsafe_allow_html=True)
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<h2>Payment Verification</h2>', unsafe_allow_html=True)

# Form input
verification_code = st.text_input("Enter 4-digit verification code", max_chars=4)



#=======================if says any other location==================
# lati1=28.456865
# longi1=77.498296
# from geopy.geocoders import Nominatim
# loc = Nominatim(user_agent="GetLoc")
# getLoc = loc.geocode('Andhra Pradesh')
#
# lati2=getLoc.latitude
# longi2=getLoc.longitude
# otpgot=1234

#=====================current===========================

import geocoder
g = geocoder.ip('me')
lati1=g.latlng[0]
longi1=g.latlng[1]
lati2 = 0
longi2 = 0
otpgot = 0

##database workss------------------------------------------------

db = sqlite3.connect("locationkey.sqlite")
cur=db.cursor()

key2=0
cur.execute('SELECT key1,lat1, long1, otp FROM locationkey ORDER BY rowid DESC LIMIT 1')
latest_entry = cur.fetchone()
# st.write(latest_entry)
if latest_entry:
    key2,lati2, longi2, otpgot= latest_entry
else:
    key2,lati2, longi2, otpgot = None,None, None, None
db.commit()

#==================================================================

dist = distance(lati1,longi1,lati2,longi2)
# st.write(dist)
# st.write(otpgot)
# st.write(lati2)
# st.write(longi2)


if dist < 2:
   # st.success("Payment verification successful!")
    if st.button("Submit"):
        if str(verification_code) == str(otpgot):
            st.success("Payment verification successful!")
            st.image("https://c8.alamy.com/comp/2J0Y4NK/happy-emoji-emoticon-showing-double-thumbs-up-like-2J0Y4NK.jpg")
        else:
            st.error("Payment Denied!")
            st.image("https://emojiisland.com/cdn/shop/products/Sad_Face_Emoji_large.png?v=1571606037")
else:
    if st.button("Submit"):
        st.write("Payment Failed")
        st.image("https://emojiisland.com/cdn/shop/products/Sad_Face_Emoji_large.png?v=1571606037")