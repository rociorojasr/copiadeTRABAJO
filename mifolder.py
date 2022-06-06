import streamlit as st
import pandas as pd
import numpy as np

st.title("      Casos positivos COVID-19", anchor = None)

st.markdown("En la presente página se visualizará distintos gráficos con datos relacionados a la evolución de los casos postivos de COVID-19.")
st.subheader('Equipo 04')
st.markdown("Integrantes:")
st.markdown("*Sandy Castillo Mallqui, Estefania Huaman Tovar, Maria Rivera Chiclla, Jackeline Roque Maceda y Heydi Surco Mamani*")

#####CONTEXTO
st.subheader("Contexto:")
st.markdown("textooooo")
from PIL import Image
image = Image.open('covid.jpg')
st.image(image)

option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Hola', 'Mobile phone'))
st.write('You selected:', option)
