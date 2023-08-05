import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from PIL import Image



st.sidebar.markdown(
    f"""
    <style>
    div.css-6qob1r {{
        background-image: linear-gradient(20deg, rgba(129,235,255,0.4) 0%, rgba(255,255,255,0) 48%);

        padding: 0;
        margin: 0;
    }}
    </style>

    """,
    unsafe_allow_html=True,
    )




with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
    
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

c1, c2 = st.columns([1, 3])
with c2:
    image = Image.open('images/Picture1.png')
    st.image(image, width=400)

with c1:
    image2 = Image.open('images/Picture2.png')
    st.image(image2, width=150)
st.title('KHARAZMI ACTIVECLAY DASHBOARD')

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{name}*')
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')


# hashed_passwords = stauth.Hasher(['Kk123456!']).generate()

tab1, tab2 = st.tabs(['Basic Information', 'Machine Learning Results'])

with tab1:
    st.subheader("Here's are some basic knowledge about activecly catalyst.")
    
with tab2:
    st.subheader('correlation matrix plot:')
    image1 = Image.open('images/Correlation2.jpg')
    st.image(image1)
    st.caption("this plot shows the pierson correlation between different attributes. higher correlation (+ or -), between two attributes means linear relationship.")
    st.write('The surface area column exhibits the highest correlation with the columns representing the initial surface area and the sum of octahedral oxides. The correlation with the initial surface area might be attributed to an increase in the initial clay surface area, leading to enhanced contact between the acidic solution and the clay, resulting in increased ion exchange and better activation of the clay. Additionally, the correlation with the sum of octahedral oxides could be due to the increased presence of exchangeable ions. As the concentration of ions like Al3+ increases, the release of these ions from the octahedral structure of clay intensifies, leading to an increase in the final surface area. ')
    
    container = st.container()
    container.write('------------------------------------')
    st.subheader('Model learning curve plot:')
    image2 = Image.open('images/learning_curve.jpg')
    st.image(image2)
    st.caption("learning curve shows the model performence based on different amount of data.")
    st.write('After data collection and preprocessing, various machine learning models were trained, and the gradient boosting model achieved the best result with an accuracy of 0.7 on the entire dataset. The above figure illustrates the learning curve of the model showing that, up to approximately 250 samples, the model performance is not satisfactory. However, as the number of data points increases, the accuracy of the model improves gradually, and its error converges.')

    container = st.container()
    container.write('------------------------------------')
    st.subheader('y_true - y_pred plot:')
    image3 = Image.open('images/pred.jpg')
    st.image(image3, width=500)
    st.caption("y_true - y_pred plot, shows that how good the trained model is, in prediction surface area of new data.")
    st.write('In the above figure, it can be observed that the data points are relatively close to the green line, which has a slope of one. This indicates that the model has performed well in predicting the outcomes. Additionally, from the learning curve, it can be seen that as the number of data points increases, the model accuracy improves, and its error decreases. This confirms the model growth and improvement with an increase in the volume of data, highlighting the significance of expanding the dataset to enhance the model performance.')

    container = st.container()
    container.write('------------------------------------')
    st.subheader('SHAP values plot:')
    image4 = Image.open('images/SHAP_beeswarm2_test2.jpg')
    st.image(image4)
    st.caption("SHAP values plot, indicates the importance of each feature, based on the trained model result and rules of game theory")
    st.write('The SHAP values (Shapley) represent the importance of each feature. It is observed that the acid concentration and the sum of octahedral oxides have the most significant impact on the surface area. Increasing their values has led to an increase in the final surface area.')

