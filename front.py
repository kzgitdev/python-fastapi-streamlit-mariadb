import streamlit as st
import random
import requests
import json
import pandas as pd
import numpy as np
from PIL import Image

page = st.sidebar.selectbox('choose your page', ['user registration', 'user list'])

st.markdown("""
# My Sample App.
***
""")

if page == 'user registration':

    st.title('user registration')
    with st.form(key='user'):
        name: str = st.text_input('name')
        data = {
          'name': name,
        }
        submit_button = st.form_submit_button(label="regist")

    if submit_button:
        url = 'http://app:8080/app/users'
        res = requests.post(
            url,
            data = json.dumps(data)
        )
        st.write('## post data')
        st.write(data)
        st.write(res.json())
        if res.status_code == 200:
            st.success('user data is registarted.')
            
        st.write(res.status_code) 
        st.json(res.json())

elif page == 'user list':

    st.title('user list')
    url = 'http://app:8080/app/users'
    st.write('## レスポンス結果')
    res = requests.get(url)
    users = res.json()
    for i in len(users):
        st.write(i)
