import streamlit as st
import pandas as pd
import joblib

#loop modal
modal = joblib.load("heart_attack_modal.pkl")
scaler = joblib.load("scaler.pkl")
expected_columns = joblib.load("columns.pkl")


st.title("Heart Stroke Prediction by Himanshu")
st.markdown("Provide the following details to check your heart stroke risk:")


#collect user input
age = st.slider("Age",18,100,40)
sex = st.selectbox("Sex",["M","F"])
chest_pain = st.selectbox("Chest pain Type",["ATA","NAP","TA","ASY"])
resting_bp = st.number_input("Resting Blood Pressure(mm Hg)",80,200,120)
cholestrol = st.number_input("Cholestrol (mg/DL)",100,600,200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL",[0,1])
resting_ecg = st.selectbox("RestingECG",["Normal","ST","LVH"])
max_hr = st.slider("Max Heart Rate",60,220,150)
exercise_angina = st.selectbox("Exercise_Induced Angina",["Y","N"])
oldpeak = st.slider("Oldpeak (ST depression)",0.0,6.0,1.0)
st_slope = st.selectbox("ST Slope",["UP","Flat","Down"])

#When Predict is clicked
if st.button("Predict"):
    
    #create a raw input dictionary
    raw_input = {
        'Age' : age,
        'Resting Bp': resting_bp,
        'Cholestrol' : cholestrol,
        'FastingBS' : fasting_bs,
        'MaxHR' : max_hr,
        'Oldpeak' : oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_'+chest_pain:1,
        'RestingECG'+ resting_ecg:1,
        'Exerciseangina_'+ exercise_angina:1,
        'ST_Slope_'+ st_slope:1
    }
    
    #create input dataframe 
    input_df = pd.DataFrame ([raw_input])
    
    
    #Fill in missing columns with 0s
    for col in  expected_columns:
        if col not in input_df.columns:
            input_df[col]= 0
            
            
            
    # recoder columns 
    input_df = input_df[expected_columns]
    
    #Scale the input
    scaled_input = scaler.transform(input_df)
    
    #Make predicition
    prediction = modal.predict(scaled_input)[0]
    
    
    #show result 
    if prediction == 1:
        st.error("⚠️High Risk OF heart Disease")
    
    else:
        st.success("✅Low risk of Heart Disease")    