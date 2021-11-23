import streamlit as st
import pandas as pd
import numpy as np
import pickle

pickle_in = open('logisticRegr.pkl', 'rb')
classifier = pickle.load(pickle_in)

st.write('Before you continue, please read the [terms and conditions](https://www.gnu.org/licenses/gpl-3.0.en.html)')
show = st.checkbox('I agree the terms and conditions')
st.title(" ~Welcome to Diabetes's Info~")
st.write("Diabetes is a disease in which your blood glucose (blood sugar) levels are too high.     Glucose comes from food and insulin is a hormone that is created     in the body to help glucose get into cells to give them energy.")
st.write("DIABETES AWARENESS BECAUSE IT MATTERS ")
vid=open("example.mp4","rb")
st.video(vid)
st.markdown("<span style=“background-color:#121922”>",unsafe_allow_html=True)
st.write("Diabetes Rates by Country 2021")
st.write("Please input country's name: (Example:India)")
c=st.text_input(" ")
sv=pd.read_csv('csvData.csv')
d=sv[sv['Country'] == c]
st.write("The number of diabeter's population is: ",d)

option = st.selectbox(
    'Select Diabetes Rates by Country 2021 ', 
    ('Top 10','Last 10'))

if option=='Top 10':
    result1 = sv.head(10)
    st.write('Top 10 Diabetes Rates: ',result1)
elif option=='Last 10':
    result2 = sv.tail(10)
    st.write('Last 10 Diabetes Rates: ',result2)
else:
    st.write("Please select")

st.write("Now, lets fill the diabetes prediction form.(Please untick hide button)")

st.sidebar.header('Diabetes Prediction')
select = st.sidebar.selectbox('Select Form', ['Form 1'], key='1')
if not st.sidebar.checkbox("Hide and Refill Form", True, key='1'):
    st.title('Diabetes Prediction(Only for females above 21years of    Age)')
    name = st.text_input("Name:")
    pregnancy = st.number_input("No. of times pregnant:")
    glucose = st.number_input("Plasma Glucose Concentration :")
    bp =  st.number_input("Diastolic blood pressure (mm Hg):")
    skin = st.number_input("Triceps skin fold thickness (mm):")
    insulin = st.number_input("2-Hour serum insulin (mu U/ml):")
    bmi = st.number_input("Body mass index (weight in kg/(height in m)^2):")
    dpf = st.number_input("Diabetes Pedigree Function:")
    age = st.number_input("Age:")
submit = st.button('Predict')
if submit:
        prediction = classifier.predict([[pregnancy, glucose, bp, skin, insulin, bmi, dpf, age]])
        if prediction == 0:
            st.write('Congratulation',name,'You are not diabetic')
        else:
            st.write(name," we are really sorry to say but it seems like you are Diabetic.")
