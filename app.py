import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dashboard de Veículos")

df = pd.read_csv("data/vehicles.csv")

st.write("Exploração interativa dos dados de veículos usados.")

# 🔹 CHECKBOX 1 - Histograma
show_hist = st.checkbox("Mostrar Histograma da Quilometragem")

if show_hist:
    st.write("Distribuição da quilometragem dos veículos")
    fig = px.histogram(df, x="odometer", title="Quilometragem")
    st.plotly_chart(fig)

# 🔹 CHECKBOX 2 - Scatter plot
show_scatter = st.checkbox("Mostrar Preço vs Quilometragem")

if show_scatter:
    st.write("Relação entre preço e quilometragem")
    fig = px.scatter(df, x="odometer", y="price",
                     title="Preço vs Quilometragem")
    st.plotly_chart(fig)