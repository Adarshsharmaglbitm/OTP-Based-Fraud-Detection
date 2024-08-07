import random
import sqlite3
import streamlit as st
import geocoder


st.header("OTP")
otp=random.randint(1000,9999)
st.header(otp)


g = geocoder.ip('me')
a=g.latlng[0]
b=g.latlng[1]
# st.write(a)
# st.write(b)


db = sqlite3.connect("locationkey.sqlite")
cur=db.cursor()

# sql_query='create table locationotpkey(parsekey int,lat1 int,long1 int,otp int)'
# cur.execute(sql_query)
parse=random.randint(1000000000000000,9999999999999000)

cur.execute('INSERT INTO locationkey(key1,lat1, long1, otp) VALUES (?,?, ?, ?)', (parse,a, b, otp))



# cur.execute('select * from locationotp')
# locations=cur.fetchall()
# st.write(locations)
db.commit()




