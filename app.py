import streamlit as st
import joblib
model_knn=joblib.load("lr_model_knn")
st.title("BMI Class Predictor")
weight=st.number_input("Weight(kg): ",min_value=48,max_value=95,value=62,step=1)
height=st.number_input("Height(cm): ",min_value=140,max_value=198,value=160,step=1)
if st.button('PREDICT'):
  op=model_knn.predict([[weight,height]])
  st.subheader("The BMI class for the person with the above specified weight and height is "+op[0])
