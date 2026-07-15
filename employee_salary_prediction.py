import os
import pandas as pd
import numpy as np
import xgboost as xgb
import streamlit as st

# Ensure the working directory is correct
os.chdir(os.path.dirname(__file__))

def main():
    html_temp = """<h1>Employee Salary Prediction</h1>"""
    model = xgb.XGBRegressor()
    model.load_model("xg_model.json")  # Ensure this file exists in the same directory
    st.markdown(html_temp, unsafe_allow_html=True)
    st.markdown("This is a simple web application that predicts the salary of an employee based on their features. Please enter the details of the employee below and click on the 'Predict' button to get the estimated salary.")
    
    
    
    p1 = st.number_input("Please enter the age of an employee (in years)",18,70,step=1)
    
    p2 = st.number_input("Please enter the years of experience of an employee",0,50,step=1)
    
    s1 = st.selectbox("Please select the education level of an employee",["High School","Bachelor's Degree","Master's Degree","PhD"])
    if s1 == "High School":
        p3 = 0
    elif s1 == "Bachelor's Degree":
        p3 = 1
    elif s1 == "Master's Degree":
        p3 = 2
    else:
        p3 = 3

    s2 = st.selectbox("Please select the department of an employee",["Operations","Marketing","Sales","IT","HR"])
    
    if s2 == "Operations":
        p4 = 0  
    elif s2 == "Marketing":
        p4 = 1
    elif s2 == "Sales":
        p4 = 2
    elif s2 == "IT":
        p4 = 3
    else:
        p4 = 4

    s3 = st.selectbox("Please select the city",["Chennai","Delhi","Mumbai","Hyderabad"])
    
    if s3 == "Chennai":
        p5 = 0
    elif s3 == "Delhi":
        p5 = 1
    elif s3 == "Mumbai":
        p5 = 2
    else:
        p5 = 3
        
    s4 = st.selectbox("Please selct the job level ",["Senior","Mid","Junior"])
   
    if s4 == "Senior":
        p6 = 0
    elif s4 == "Mid":
        p6 = 1
    else:
        p6 = 2
        
    s5 = st.selectbox("Please enter the gender of the amployee",["Male","Female"])
    
    if s5 == "Male":
        p7 = 0
    else:
        p7 = 1
        
    p8 = st.number_input("Enter the performance rating of the employee", 1, 5, step=1)  
    p9 = st.number_input("Enter the number of certificates employee has", 0, 10, step=1)   
    p10 = st.number_input("Enter the overtime hours", 0, 100, step=1)
    
    s6 = st.selectbox("Please tell whether employee is doing remote work or not",["Yes","No"])
    
    if s6 == "Yes":
        p11 = 0
    else:
        p11 = 1
        
    p12 = st.number_input("Enter the Company tenure",0,20,step=1)
    
    p13 = st.number_input("Enter the number of projects completed",0,50,step=1)
    
    p14 = st.number_input("Enter the skill score of the employee",0,100,step=1)

    
    data_new = pd.DataFrame({
    'Age':p1,
    'Education':p3,
    'Gender':p7,
    'Department':p4,
    'Job_Level':p6,
    'Experience_Years':p2,
    'Performance_Rating':p8,
    'Certifications':p9,
    'Overtime_Hours':p10,
    'Remote_Work':p11,
    'City':p5,
    'Company_Tenure':p12,
    'Projects_Completed':p13,
    'Skill_Score':p14
    },index=[0])  
          
         
            
    if st.button("Predict"):
        prediction = model.predict(data_new)
        st.success(f"The estimated salary of an employee is: {prediction[0]:.2f} lakhs")
 

if __name__ == '__main__':
    main()