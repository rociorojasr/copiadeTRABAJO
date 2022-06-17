import streamlit as st
import pandas as pd
import numpy as np

n = st.slider("n", 5, 100, step=1)
chart_data=pd.DataFrame(np.random.randn(n),colums=["data"])
st.line_chart(chart_data)
