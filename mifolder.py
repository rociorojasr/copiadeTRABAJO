import streamlit as st
import pandas as pd
import numpy as np

st.title("EQUIPO 04 - VISUALIZACION DE DATA")

st.text("En la presente página se visualizará distintos gráficos con datos relacionados a la evolución de los casos postivos de COVID-19.")

option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Hola', 'Mobile phone'))

st.write('You selected:', option)
