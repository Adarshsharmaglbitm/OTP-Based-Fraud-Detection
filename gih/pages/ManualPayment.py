import streamlit as st
from twilio.rest import Client
import time
import random

def otpsendsend(OTP):
    time.sleep(2)
    mobile = "7985361213"
    account_sid = 'ACa395fb7ffab5fd7d43872a369e4d7301'
    auth_token = '3dcd625909d1749334e3c26032fbcca2'
    client = Client(account_sid, auth_token)
    msg = client.messages.create(body="this is your" + str(OTP),
                                 from_='+1 209 882 4995',
                                  to="+91" + mobile)
    st.success("OTP SEND SUCCESFULLY CHECK IN YOUR PHONE")


OTP=random.randint(1000,9999)
otpsendsend(OTP)
st.write("Your OTP is: " + str(OTP))
verification_code = st.text_input("Enter 4-digit verification code", max_chars=4)
st.write("Your verification code is: " + str(verification_code))
if st.button("Verify"):
    if str(verification_code) == str(OTP):
        st.success("Verification")
    else:
        st.error("Failed")