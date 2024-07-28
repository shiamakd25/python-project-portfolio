import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/title_photo.jpg")

with col2:
    st.title("Shiamak Das")
    description = """Hi, I am Shiamak. This is a project portfolio consisting of various Python projects spanning across many Python topics. These topics include PDF documents and operations, automating emails, managing and visualizing data, using APIs, machine learning, web scraping, OOP, SQL databases, web development with Django and Flask, data science, and Python packages."""
    st.info(description)
