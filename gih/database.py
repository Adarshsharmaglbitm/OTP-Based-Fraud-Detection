import random
import sqlite3
import streamlit as st

db = sqlite3.connect("locationkey.sqlite")
cur=db.cursor()

# sql_query='create table locationkey(key1 int,lat1 int,long1 int,otp int)'
# cur.execute(sql_query)

parse=random.randint(1000000000000000,9999999999999000)
# # str="EabcAEBZ"+str(parse)
cur.execute('INSERT INTO locationkey (key1, lat1, long1, otp) VALUES (?, ?, ?, ?)', (parse, 28.4444, 70.5555, 1234))
# # cur.execute('SELECT lat1, long1, otp FROM locationotp ORDER BY rowid DESC LIMIT 1')
# # latest_entry = cur.fetchone()
# # st.write(latest_entry)
# # cur.execute('select * from location ')
# # locations=cur.fetchall()
# # st.write(locations)
db.commit()




