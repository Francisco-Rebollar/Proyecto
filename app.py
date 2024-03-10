import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Analisis base "vehicles_us.csv"')

st.write('Selecciona el grafica que deseas visualizar')    

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Histograma del odómetro de los anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer", title='Histograma del Odómetro', labels={'odometer': 'Odómetro'})

    # personalizar colores y formato
    fig.update_layout(
        xaxis_title='Odómetro',
        yaxis_title='Frecuencia',
        template='plotly_dark'  # puedes cambiar a otros temas disponibles en Plotly
    )

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Construir gráfico de dispersión')  # crear un botón

if disp_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Gráfico de dispersión entre el odómetro y el precio de los anuncios de venta de coches')

    # crear un gráfico de dispersión
    fig2 = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión


    

