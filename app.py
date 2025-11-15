import streamlit as st
import pandas as pd
import joblib

# Load models and scaler
model = joblib.load('Logestic_Heart.pkl')
scaler = joblib.load('scaler_Heart.pkl')
expected_columns = joblib.load('columns_Heart.pkl')

# App title
st.title('Heart Stroke Prediction By Chaitanya')
st.markdown('Provide The Following Details:')

# Input fields
age = st.slider('Age', 18, 100, 40)
sex = st.selectbox("Sex", ['M', 'F'])
chest_pain = st.selectbox('Chest Pain Type', ['ATA', 'NAP', 'TA', 'ASY'])
resting_BP = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
Cholesterol = st.number_input('Cholesterol (mg/dl)', 100, 600, 200)
Fasting_BS = st.selectbox('Fasting Blood Sugar > 120 mg/dL', [0, 1])
Resting_ecg = st.selectbox("Resting ECG", ['Normal', 'ST', 'LVH'])
Max_HR = st.slider("Max Heart Rate", 60, 220, 150)
Exercise_Angina = st.selectbox('Exercise-Induced Angina', ['Y', 'N'])
oldpeak = st.slider('Oldpeak (ST Depression)', 0.0, 6.0, 1.0)
st_slope = st.selectbox("ST Slope", ['UP', 'Flat', 'Down'])

# Prediction
if st.button("Predict"):
    raw_input = {
        'Age': age,
        'RestingBP': resting_BP,
        'Cholesterol': Cholesterol,
        'FastingBS': Fasting_BS,
        'MaxHR': Max_HR,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + Resting_ecg: 1,
        'ExerciseAngina_' + Exercise_Angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    # Convert to DataFrame
    input_df = pd.DataFrame([raw_input])

    # Add missing columns
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0
    input_df = input_df[expected_columns]

    # Scale and predict
    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]

    # Show result
    if prediction == 1:
        st.error('High Risk of Heart Disease')
    else:
        st.success('Low Risk of Heart Disease')
