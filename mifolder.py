import streamlit as st
import pandas as pd}
import gdown
#id = 1Gu65mnJ_lxE0BdbkL1nTq5qaFJ1dJ9tq
@st.experimental_memo
def download_data():
 #https://drive.google.com/uc?id=YOURFILE
 url = 'https://drive.google.com/uc?id=1Gu65mnJ_lxE0BdbkL1nTq5qaFJ1dJ9tq'
 output = 'data.csv'
 gdown.download(url,output,quiet = False)

download_data()
data = pd.read_csv('data.csv', sep = ';', nrows = 1000000, parse_dates=['FECHA_CORTE', 'FECHA_RESULTADO'])


st.title("      Casos positivos COVID-19", anchor = None )
st.markdown("En la presente página se visualizará distintos gráficos con datos relacionados a la evolución de los casos postivos de COVID-19.")
st.subheader('Equipo 04')
st.markdown("*Sandy Castillo Mallqui, Estefania Huaman Tovar, Maria Rivera Chiclla, Jackeline Roque Maceda y Heydi Surco Mamani*")


#####CONTEXTO
st.subheader("Contexto:")
st.markdown("textooooo")
from PIL import Image    ######Insertar imagen en streamlit
image = Image.open('covid.jpg')

st.image(image)
st.dataframe(data.head(20))
metodo=data['METODODX']

