import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.header('Análisis Exploratorio de Vehículos - Proyecto Streamlit')

# Leer datos
car_data = pd.read_csv('vehicles_us.csv')

# Botón para histograma
if st.button('Construir histograma'):
    st.write('Histograma de la distribución del odómetro')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig, use_container_width=True)

# Botón para gráfico de dispersión
if st.button('Construir gráfico de dispersión'):
    st.write('Relación entre precio y odómetro')
    fig = go.Figure(data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])
    fig.update_layout(title_text='Precio vs Odómetro')
    st.plotly_chart(fig, use_container_width=True)
