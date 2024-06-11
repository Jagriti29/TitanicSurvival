import streamlit as st
import pickle

# Load the model
model_path = 'titanic_model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

st.title('Titanic Survival Prediction')
st.write('Enter the details of the passenger to predict if they survived.')

# Input fields
pclass = st.selectbox('Class', [1, 2, 3])
gender = st.selectbox('Gender', ['male', 'female'])
age = st.slider('Age', 0, 85, 25)

if gender == 'Male':
    gender = 1
else:
    gender = 0

if st.button('Predict'):
    prediction = model.predict([[pclass, age, gender]])
    result = 'Survived' if prediction[0] == 1 else 'Not Survived'
    st.write(f'The passenger is predicted to have {result}.')

    

