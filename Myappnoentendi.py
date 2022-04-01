import streamlit as st
st.title("mi primer app")
click=st.button("ok")
st.write("el valor de click es:pescado",click)
if click==True:
    st.image("descarga.jpg")
import pandas as pd
#Las primeras 3 lineas son para el primer ejercicio
#df=pd.read_csv("https://raw.githubusercontent.com/quantum-apps/mapa/main/data.csv")
#st.write(df)
#st.map(df)
#st.text("hola mundo")
#st.latex("\int_1^6")
#st.markdown("#titulo")
#st.markdown("este es una viñeta")
num1 = st.slider('Elige el numero 1', 0, 100, 25)
num2 = st.slider('Elige el numero 2', 0, 100, 25)
suma=num1+num2
st.write("La suma de",num1,"y",num2, 'es:',suma)
