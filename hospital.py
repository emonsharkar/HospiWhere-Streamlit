import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv('dataset_hospital_organized.csv')

# Sidebar input fields
st.sidebar.header('Enter Preferences')
district = st.sidebar.selectbox('District', df['District'].unique())
specialization = st.sidebar.selectbox('Specialized In', df['Specialized In'].unique())

# Function to recommend hospitals based on user input
def recommend_hospitals(district, specialization):
    filtered = df[(df['District'] == district) & (df['Specialized In'] == specialization)]
    return filtered

# Function to display hospital details textually
def display_hospital_details(hospital):
    details_string = f"""
    **Name:** {hospital['Name']}
    **Place:** {hospital['Place']}
    **District:** {hospital['District']}
    **Specialized In:** {hospital['Specialized In']}
    **Overall Rating:** {hospital['Overall Rating']}
    """
    # Now assign the formatted string to details_text
    return details_string  # Return the formatted string

# Main content
st.title('Hospital Recommendation System')

# Initialize empty dataframe to store recommended hospitals
recommended_hospitals = pd.DataFrame()

# When submit button is clicked
if st.button('Submit'):
    # Get recommended hospitals based on user input
    recommended_hospitals = recommend_hospitals(district, specialization)

    # Display recommended hospitals with details
    st.subheader('Recommended Hospitals')
    if recommended_hospitals.empty:
        st.write('No hospitals found matching the selected criteria.')
    else:
        for idx, (hospital_id, row) in enumerate(recommended_hospitals.iterrows(), 1):
            # Combine hospital name and details for button text
            hospital_name = row['Name']
            details_string = display_hospital_details(row)  # Call function to get details

            # Display hospital name and details textually
            st.write(f"{idx}. {hospital_name}")
            st.write(details_string)



