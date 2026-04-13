import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dashboard de Dados")

uploaded_file = st.file_uploader("Carregar CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Dados")
    st.dataframe(df)

    # KPIs
    st.subheader("Indicadores")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total de Registos", len(df))

    with col2:
        if df.select_dtypes(include='number').shape[1] > 0:
            total = df.select_dtypes(include='number').sum().sum()
            st.metric("Soma Total", f"{total:,.0f}")

    with col3:
        if df.select_dtypes(include='number').shape[1] > 0:
            media = df.select_dtypes(include='number').mean().mean()
            st.metric("Média", f"{media:,.2f}")

    # Gráfico
    st.subheader("Gráfico")

    x = st.selectbox("Eixo X", df.columns)
    y = st.selectbox("Eixo Y", df.columns)

    fig = px.bar(df, x=x, y=y)

    st.plotly_chart(fig)

else:
    st.write("Carrega um ficheiro CSV")