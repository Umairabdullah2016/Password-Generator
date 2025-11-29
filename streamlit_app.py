import streamlit as st
import random
import string

def random_string(length=12):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

st.title("Password")

length = st.number_input("Length", min_value=1, max_value=200, value=12)

if st.button("Generate Password"):
    result = random_string(length)
    st.success(result)
