import pandas as pd
import streamlit as st
import plotly.express as px

datos = pd.read_csv('vehicles_us.csv')

#print(datos.head())

st.title('Analisis de anuncios de ventas de autos')

st.header('Analisis exploratorio de datos')

boton_hist = st.checkbox('Mostrar histograma de km recorridos')

if boton_hist:
    fig = px.histogram(datos['odometer'])
    st.plotly_chart(fig)