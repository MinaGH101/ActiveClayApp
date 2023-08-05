import streamlit as st 
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import joblib


st.set_page_config(
    page_title="Kharazmi Activeclay Dashboard",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title('🚀 Prediction Mode')
st.sidebar.write("""
predicts BET (m2/g) based on raw clay analysis and process parameters.
""")

st.markdown("""
        <style>
               .css-12oz5g7 {
                    padding-top: 1rem;
                    padding-bottom: 10rem;
                    padding-left: 2rem;
                    padding-right: 0rem;
                }
               .css-12oz5g7 {
                    padding-top: 2rem;
                    padding-right: 1rem;
                    padding-bottom: 2rem;
                    padding-left: 2rem;
                }
                .css-18e3th9 {
                    padding-top: 2rem;
                    padding-right: 4rem;
                    padding-bottom: 2rem;
                    padding-left: 4rem;
                }
        </style>
        """, unsafe_allow_html=True)

model  = joblib.load('../xgb.pkl')

col1, col2, col3, col4 = st.columns([1.5, 1.5,  1 ,1])

with col1:
    
    f13 = st.select_slider('Acid Type', options=['H2SO4', 'HCl', 'HNO3'])
    f14 = st.slider('Acid Normal', 0.0, 20.0, 2.5, step=0.25)
    f15 = st.slider('wt clay (g)/ V acid (cc)', 0.0, 2.0, 0.05, step=0.01)

    
with col2:
    f16 = st.slider('T(°C)', 50.0, 100.0, 95.0, step=0.25)
    f17 = st.slider('Time (h)', 0.0, 20.0, 3.0, step=0.25)
    f18 = st.slider('highest seen Temp', 50.0, 400.0, 180.0, step=10.0)


    
with col3:
    f1 = st.number_input("Clay MW", value=360.36, key="Clay MW")
    f2 = st.number_input("initial BET (m2/g)", value=33.3, key="initial BET (m2/g)")
    f3 = st.number_input("d (001) angstrom", value=12.76, key="d (001) angstrom")
    f4 = st.number_input("initial Al2O3", value=12.7, key="initial Al2O3")
    f5 = st.number_input("initial Fe2O3", value=3.7, key="initial Fe2O3")
    f6 = st.number_input("initial CaO", value=5.4, key="initial CaO")

with col4:
    f7 = st.number_input("initial MgO", value=2.8, key="initial MgO")
    f8 = st.number_input("initial K2O", value=1.7, key="initial K2O")
    f9 = st.number_input("initial Na2O", value=1.5, key="initial Na2O")
    f10 = st.number_input("Octa Oxides Sum", value=19.2, key="Octa Oxides Sum")
    f11 = st.number_input("Iintra layer Oxides Sum", value=8.6, key="Iintra layer Oxides Sum")
    f12 = st.number_input("SiO2/Al2O3", value=4.54, key="SiO2/Al2O3")
    

if f13 == 'H2SO4':
    f13_ = 98.08
elif f13 == 'HCl':
    f13_ = 36.46
else:
    f13_ = 63.1

X = np.array([f1, f2, f3, f4, f5, f6, f7, f8, f9,
                f10, f11, f12, f13_, f14, f15, f16, f17, f18], dtype='float64').reshape(1, 18)

y_pred = model.predict(X)

st.subheader(f'Predicted BET: {np.round(y_pred, 1)} (m2/g)')