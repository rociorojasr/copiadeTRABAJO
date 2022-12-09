import gdown
import streamlit as st
import pandas as pd

#id=1WUcvXmNN6nuDbtv0crOe2qDrbc9stWjA
@st.experimental_memo
def download_data():
  #https://drive.google.com/uc?id=MIOOO
  url="https://drive.google.com/uc?id=1WUcvXmNN6nuDbtv0crOe2qDrbc9stWjA"
  output='data.csv'
  gdown.download(url,output,quiet= False)
	
download_data()
df = pd.read_csv('data.csv',sep = ';',nrows=1000000,parse_dates=['Departamento', '#Centro de vacunación'])
st.dataframe(data.head(5))



