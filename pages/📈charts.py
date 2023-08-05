import streamlit as st 
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import KNNImputer
from PIL import Image

st.set_page_config(
    page_title="Kharazmi Activeclay Dashboard",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title('📈 Plot Parameters')
st.write("""
plot activeclay dataset parameters and see the trends...
""")

D1 = pd.read_excel('./ACPP.xlsx', sheet_name='Sheet5')
D = D1.to_numpy(dtype='float64')
clay = D[: , :11]
acid = D[: , 11:13]
process = D[:, 13:]
imputer = KNNImputer(n_neighbors=5)
clay = imputer.fit_transform(clay)
acid = imputer.fit_transform(acid)
process = imputer.fit_transform(process)
Data = np.concatenate((clay, acid, process), axis= 1)
Data = pd.DataFrame(Data, columns = D1.columns)
Data['BET_difference (%)'] = ((Data['BET'] - Data['initial BET (m2/g)'])*100)/Data['initial BET (m2/g)']
Data = Data.drop(['Clay MW', 'Acid MW'] ,axis =1)

X_name = st.sidebar.selectbox(
    'Select X-axis',
    (Data.columns))

y_name = st.sidebar.selectbox(
    'Select Y-axis',
    (Data.columns))

color = st.sidebar.selectbox(
    'Select a color',
    ('blue', 'red', 'forestgreen', 'purple', 'blueviolet', 'aqua'))

def get_dataset(X_name, y_name):
    X = Data[X_name]
    y = Data[y_name]
    return X, y

# C = st.sidebar.slider('C', 0.01, 10.0)

X, y = get_dataset(X_name, y_name)

col1, col2 = st.columns([2.5, 3])
with col1:
    
    with st.form("my_form", clear_on_submit=False):
        X_min = st.number_input("X_min", value=X.min(), key="X_min")
        X_max = st.number_input("X_max", value=X.max(), key="X_max")
        y_min = st.number_input("y_min", value=y.min(), key="y_min")
        y_max = st.number_input("y_max", value=y.max(), key="y_max")
        
        if X_min:
            Xmin = X_min
        else:
            Xmin = X.min()
            
        if X_max:
            Xmax = X_max
        else:
            Xmax = X.max()
        
    #### 
        if y_min:
            ymin = y_min
        else:
            ymin = y.min()
            
        if y_max:
            ymax = y_max
        else:
            ymax = y.max()

        reset_button = st.form_submit_button("Set / Reset")



with col2:

        
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.scatter(X, y, color=color)
    ax.set_xlabel(X_name)
    ax.set_ylabel(y_name)
    plt.xlim(Xmin, Xmax)
    plt.ylim(ymin, ymax)
    # transform = ax.transAxes
    fig.tight_layout()
    st.pyplot(fig)
