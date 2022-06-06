import streamlit as st
import pandas as pd
import numpy as np

st.title("EQUIPO 04 - VISUALIZACION DE DATA")

st.text("HOLA")

option = st.selectbox(
     'How would you like to be contacted?',
     ('Email', 'Hola', 'Mobile phone'))

st.write('You selected:', option)
