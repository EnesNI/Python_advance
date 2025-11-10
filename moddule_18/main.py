import pandas as pd
import streamlit as st

st.header("Display Data")

data = pd.DataFrame({
    'Name' : ['Blini','Enes','Mark'],
    'Age' : [19,20,21],
    'City' : ['Prishtina','Feri' , 'DWAA']
})

st.dataframe(data)