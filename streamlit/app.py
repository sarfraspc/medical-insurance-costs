import streamlit as st
import joblib
import numpy as np

model=joblib.load('../data/random_forest.joblib')

st.title('Medical Insurance Cost Predictor')
st.markdown("Predict insurance charges based on personal information")

age=st.number_input("Age", min_value=18, max_value=100, value=30, step=1)
sex_input=st.selectbox('Sex',['male','female'])
sex = 1 if sex_input == 'male' else 0
bmi = st.number_input("BMI", 10.0, 60.0, 25.0)
children = st.slider("Number of Children", 0, 5, 0)
smoker_input = st.selectbox("Smoker", ['yes', 'no'])
smoker = 1 if smoker_input == 'yes' else 0
smoker_bmi=smoker*bmi
smoker_children=smoker*children
region_northwest=0
region_southeast=1
region_southwest=0

input_data=np.array([[age,sex,bmi,children,smoker,region_northwest,region_southeast,region_southwest,smoker_bmi,smoker_children
                      ]])

if st.button('Predict Charges'):
    log_prediction=model.predict(input_data)[0]
    charges=np.expm1(log_prediction)
    st.success(f'Estimated Charges:${charges:.2f} per year')
