import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv') # Leo los datos


st.title('Bienvenido a mi proyecto del Sprint_7') # Título de la aplicación
st.subheader('Este es un análisis exploratorio de datos del conjunto de datos de anuncios de venta de coches en Estados Unidos.') # Descripción


build_histogram = st.checkbox('Mostrar histograma') # Creo el botón

if build_histogram: # Al hacer clic en el botón
    # Escribir un mensaje
    st.header('Histograma de vehiculos por `kilometraje`')

    # Creo el histograma
    fig = px.histogram(car_data, x = "odometer", 
                       labels={'odometer':'Kilometraje'}) # Etiqueta del eje x
    # Muestro un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


build_scatter = st.checkbox('Mostrar diagrama de dispersión') # Creo otro botón

if build_scatter: # Al hacer clic en el botón
    # Escribir un mensaje
    st.header('Diagrama de dispersión de `precio` vs `kilometraje`')

    # Creo el diagrama de dispersión
    fig = px.scatter(car_data, x="odometer",
                     y="price",
                     labels={'odometer':'Kilometraje', 'price':'Precio'}) # Etiquetas de los ejes

    # Muestro un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)