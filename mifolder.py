import streamlit as st
import pandas as pd
import numpy as np

st.title("EQUIPO 07 - VISUALIZACION DE DATA")

option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Hola', 'Mobile phone'))

st.write('You selected:', option)

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
     # Can be used wherever a "file-like" object is accepted:
     dataframe = pd.read_csv(uploaded_file)
     st.write(dataframe)
