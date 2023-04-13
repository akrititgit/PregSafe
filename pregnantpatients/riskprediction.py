# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 12:07:48 2022

@author: dell
"""

import numpy as np
import pickle
import streamlit as st

loaded_model=pickle.load(open('C:/Users/dell/Desktop/pregnantpatients/trained_model.sav','rb'))
def health_risks_prediction(inpArray):
    inpFrame=['Enter Age of Patient:','Enter systolic Blood Pressure of Patient:','Enter Diastolic Blood Pressuree of Patient:','Enter Blood Glucose Level of Patient:','Enter Body Temperarature of  Patient:','Enter Heart Rateof Patient:',]
    inpArray=list()
    for i in  range(6):
      temp=input(inpFrame[i])
      inpArray.append(float(temp))
    
    patientPredict=loaded_model.predict([inpArray])
    #print("________________________________________")
    if patientPredict[0]==1.0:
        return ("Risk Level of patient is Low :) You are Safe",patientPredict[0])
    elif patientPredict[0]==2.0:
        return ("Risk Level of patient is Medium:) Need to take rest and take care of yourself", patientPredict[0])
    elif  patientPredict[0]==3.0:
        return ("Risk Level of patient is High:| Need to consult to the doctor", patientPredict[0])
    #print('-----------------------------------------')
def main():
    #giving a title
    st.title('Predicting Health Risks for Pregnant Patients Web App')
     # getting the input data from the user
    Age=st.text_input('Age of the Patient')
    SystolicBP=st.text_input('Systolic BP of Patient')
    DiastolicBP=st.text_input('Diastolic BP of the Patient')
    BS=st.text_input('Blood glucose Levels of the Patient')
    BodyTemp=st.text_input('Body Temp of the Patient')
    HeartRate=st.text_input('Heart Rate of the Patient')
    # code for Prediction
    diagnosis=''
    # creating a button for Prediction
    if st.button('Health Risks test Result'):
        diagnosis=health_risks_prediction([Age,SystolicBP,DiastolicBP,BS,BodyTemp,HeartRate])
    st.success(diagnosis)
    
if __name__=='__main__':
    main()
    