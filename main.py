import streamlit as st
import pickle
import pandas as pd

model = pickle.load(open('Titanic_Model.pkl', 'rb'))
scaler = pickle.load(open('Titanic_Scaler.pkl', 'rb'))

st.title("Titanic's Passengers Survivy Prediction\n Tell Me about the details of the passenger\n and I tell You if the passenger has survived or not")

Sex =  st.selectbox("What is Your Gender ?", options=["Male" , "Female"])
Sex = 1 if Sex == "Male"  else  0

Age  = st.number_input("What is Your Age \'in Years\' like :- 1.5 years? " , min_value=0.1 ,  step=0.1, format="%.2f")

Embarked = st.selectbox("What is the port where a passenger boarded the Titanic ?" , options=["Cherbourg, France" , "Queenstown (now Cobh), Ireland" , "Southampton, England"])
Embarked = int(0) if Embarked == "Southampton, England" else int(1) if Embarked == "Cherbourg, France" else int(2)

SibSp = st.number_input("what is the  number of siblings\'Brothers or sisters\' \n OR spouses \'Husband or wife\' a passenger had on the Titanic. " , min_value = 0  , step = 1)

Pclass  = st.selectbox("What is the ticket class of the passenger ?"  , options = ["First Class" , "Second Class" , "Third Class"])

Pclass = int(1) if Pclass == "First Class"  else int(2) if Pclass == "Second Class" else int(3)

Parch  = st.number_input("How many parents\'Mother or father\' or children \'Son, daughter, stepchildren, or adopted children\' a passenger had on the Titanic." , min_value = 0  , step = 1)

# '', '', '', '', '', ''
if st.button("Predict The Survival State"):
    input_data = pd.DataFrame([{
    "Pclass": Pclass,
    "Sex": Sex,
    "Age": Age,
    "SibSp": SibSp,
    "Parch": Parch,
    "Embarked": Embarked
     }])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled) 
    result = " already Survived " if prediction == 1 else " not Survived "
    st.success(f"The Passenger has {result} from Titanic")
    