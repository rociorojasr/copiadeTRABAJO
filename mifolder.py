import streamlit as st
import pandas as pd
import numpy as np
import urllib.request
@st.experimental_memo
def download_data():
 url = 'https://files.minsa.gob.pe/s/eRqxR35ZCxrzNgr/download'
 filename = 'data.csv'
 urllib.request.urlretrieve(url, filename)
download_data()
pandas.read_csv(‘data.csv’)

st.title("      Casos positivos COVID-19", anchor = None)

st.markdown("En la presente página se visualizará distintos gráficos con datos relacionados a la evolución de los casos postivos de COVID-19.")
st.subheader('Equipo 04')
st.markdown("*Sandy Castillo Mallqui, Estefania Huaman Tovar, Maria Rivera Chiclla, Jackeline Roque Maceda y Heydi Surco Mamani*")

#####CONTEXTO
st.subheader("Contexto:")
st.markdown("textooooo")
from PIL import Image    ######Insertar imagen en streamlit
image = Image.open('covid.jpg')
st.image(image)

######Codigo para insertar dataframe (FALTA)

option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Hola', 'Mobile phone'))
st.write('You selected:', option)


