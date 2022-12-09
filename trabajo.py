import gdown
import streamlit as st
import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts
from streamlit_echarts import st_echarts
####################################################################################
##id = 1Gu65mnJ_lxE0BdbkL1nTq5qaFJ1dJ9tq
#@st.experimental_memo
#def download_data():
#     url = "https://drive.google.com/uc?id=1Gu65mnJ_lxE0BdbkL1nTq5qaFJ1dJ9tq"
###########################################

#id=13iNig4VIvt5Gm0znUt2eq3_YnGCgCQHM
@st.experimental_nemo
def download_data():
	#https://drive.google.com/uc?id=MIOOO
	url="https://drive.google.com/uc?id=13iNig4VIvt5Gm0znUt2eq3_YnGCgCQHM"
	output="data.csv"
	gdown.download(url,output,quiet=False)
download_data()
#df = pd.read_csv(r'C:\Users\51952\Downloads\PositivosCovid\positivos_covid.csv',sep=";", skip_blank_lines=True, parse_dates=['id_centro_vacunacion', 'id_eess'])
df = pd.read_csv('data.csv',sep = ";",  skip_blank_lines=True, nrows=1000,parse_dates=['id_centro_vacunacion', 'id_eess'])
st.dataframe(data.head(20))
#########################################



