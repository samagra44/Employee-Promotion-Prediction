import streamlit as st
import numpy as np
import pickle


# Load the pre-trained model
with open('emp_promotion_prediction.pkl', 'rb') as file:
    rfc_random = pickle.load(file)

st.set_page_config(
    page_title="Employee Promotion Prediction",
    page_icon="🚀",
    layout="wide",
)
st.header("Enter Employee Details for Prediction")
# Creating dropdowns and input fields for each feature
department_options = {'Analytics': 6, 'Finance': 5, 'HR': 1, 'Legal': 2, 'Operations': 4,
                       'Procurement': 0, 'R&D': 3, 'Sales & Marketing': 7, 'Technology': 8}
department = st.selectbox('Department:', list(department_options.keys()), index=0)

education_options = {"Bachelor's": 2, "Master's & above": 0, 'Below Secondary': 1}
education = st.selectbox('Education:', list(education_options.keys()), index=0)

gender_options = {'Male': 1, 'Female': 0}
gender = st.selectbox('Gender:', list(gender_options.keys()), index=0)

recruitment_channel_options = {'Other': 2, 'Sourcing': 0, 'Referred': 1}
recruitment_channel = st.selectbox('Recruitment Channel:', list(recruitment_channel_options.keys()), index=0)

no_of_trainings = st.slider('No of Trainings:', min_value=1, max_value=10, value=1)
age = st.slider('Age:', min_value=18, max_value=60, value=35)
previous_year_rating = st.slider('Previous Year Rating:', min_value=1, max_value=5, value=5)
length_of_service = st.slider('Length of Service:', min_value=1, max_value=20, value=3)
awards_won = st.checkbox('Awards Won')
avg_training_score = st.slider('Avg Training Score:', min_value=0, max_value=100, value=50)

# Create a submit button
submit_button = st.button('Submit')

# Make a prediction function based on the selected values
def make_prediction():
    awards_won_value = 1 if awards_won else 0

    input_data = {
        'department': department_options[department],
        'education': education_options[education],
        'gender': gender_options[gender],
        'recruitment_channel': recruitment_channel_options[recruitment_channel],
        'no_of_trainings': no_of_trainings,
        'age': age,
        'previous_year_rating': previous_year_rating,
        'length_of_service': length_of_service,
        'awards_won': awards_won_value,
        'avg_training_score': avg_training_score
    }

    input_array = [[input_data['department'], input_data['education'], input_data['gender'],
                    input_data['recruitment_channel'], input_data['no_of_trainings'], input_data['age'],
                    input_data['previous_year_rating'], input_data['length_of_service'], input_data['awards_won'],
                    input_data['avg_training_score']]]

    prediction = rfc_random.predict(input_array)
    st.write("Model Prediction:", prediction[0])
    if prediction[0] == 0:
        st.write("Employee Is Promoted")
    else:
        st.write("Employee Is Not Promoted")

# Trigger the prediction when the submit button is clicked
if submit_button:
    make_prediction()
