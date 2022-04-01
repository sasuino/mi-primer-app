import streamlit as st
st.title("mi primer app")
#st.button("ok")
import pandas as pd
df=pd.read_csv("https://raw.githubusercontent.com/quantum-apps/mapa/main/data.csv")
st.write(df)
st.map(df)
