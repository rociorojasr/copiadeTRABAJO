import gdown
import streamlit as st
import pandas as pd
import numpy as np
#id=1WUcvXmNN6nuDbtv0crOe2qDrbc9stWjA
@st.experimental_memo
def download_data():
	#https://drive.google.com/uc?id=MIOOO
	url="https://drive.google.com/uc?id=1WUcvXmNN6nuDbtv0crOe2qDrbc9stWjA"
	output="data.csv"
	gdown.download(url,output,quiet= False)
download_data()
df = pd.read_csv('data.csv',sep = ";",  skip_blank_lines=True, nrows=25,parse_dates=['Departamento', '#Centro de vacunación'])
st.dataframe(data.head(5))



