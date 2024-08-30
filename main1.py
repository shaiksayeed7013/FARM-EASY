import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier

# Load models and encoders
crop_model = joblib.load('crop_model.pkl')
fertilizer_model = joblib.load('fertilizer_model.pkl')
le_crop = joblib.load('le_crop.pkl')
le_soil = joblib.load('le_soil.pkl')

# Streamlit app
st.set_page_config(page_title="EASYFARM", layout="centered", initial_sidebar_state="expanded")
st.title("EASYFARM")

st.sidebar.title("Navigation")
option = st.sidebar.radio("Go to", ["Home", "Crop Recommendation", "Fertilizer Recommendation", "Input References", "Suggestions"])

if option == "Home":
    st.header("Welcome to EASYFARM!")
    st.write("This application helps farmers with crop and fertilizer recommendations based on their inputs.")
    st.image("D:/python/FARMEASY/Image.jpeg", use_column_width=True)  # Add your image path here

elif option == "Crop Recommendation":
    st.header("Crop Recommendation")
    N = st.number_input('Enter Nitrogen (N in Kg/ha)', min_value=0.0, max_value=150.0)
    P = st.number_input('Enter Phosphorus (P in Kg/ha)', min_value=0.0, max_value=200.0)
    K = st.number_input('Enter Potassium (K in Kg/ha)', min_value=0.0, max_value=250.0)
    temperature = st.number_input('Enter Temperature (in Celsius)', min_value=0.0, max_value=50.0, format="%.2f")
    humidity = st.number_input('Enter Humidity (in %)', min_value=0.0, max_value=100.0, format="%.2f")
    ph = st.number_input('Enter pH value', min_value=0.0, max_value=14.0, format="%.2f")
    rainfall = st.number_input('Enter Rainfall (in mm/year)', min_value=0.0, max_value=3000.0, format="%.2f")

    # Validate inputs
    if st.button("Predict Crop"):
        data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        prediction = crop_model.predict(data)
        
        st.subheader("Recommended Crop:")
        st.success(prediction[0])
        
        out_of_range = False
        if N > 150:
            st.warning("Nitrogen level is too high. To reduce Nitrogen, consider planting leguminous crops or using organic manure.")
            out_of_range = True
        if P > 200:
            st.warning("Phosphorus level is too high. To reduce Phosphorus, consider avoiding phosphorus-rich fertilizers.")
            out_of_range = True
        if K > 250:
            st.warning("Potassium level is too high. To reduce Potassium, consider using crops that uptake high potassium.")
            out_of_range = True
        if ph < 6.0:
            st.warning("Soil is too acidic. To increase pH, consider using lime.")
            out_of_range = True
        if ph > 8.5:
            st.warning("Soil is too alkaline. To decrease pH, consider using sulfur or organic compost.")
            out_of_range = True
        if temperature < 15:
            st.warning("Temperature is too low for most crops. Consider greenhouse farming to regulate temperature.")
            out_of_range = True
        if temperature > 35:
            st.warning("Temperature is too high. Ensure adequate irrigation and mulching to protect crops.")
            out_of_range = True
        if humidity < 40:
            st.warning("Humidity is too low. Consider using irrigation to increase humidity.")
            out_of_range = True
        if humidity > 70:
            st.warning("Humidity is too high. Ensure proper ventilation to reduce fungal diseases.")
            out_of_range = True
        if rainfall < 500:
            st.warning("Rainfall is too low. Consider using drought-resistant crops or irrigation.")
            out_of_range = True
        if rainfall > 1500:
            st.warning("Rainfall is too high. Ensure proper drainage to prevent waterlogging.")
            out_of_range = True

        if out_of_range:
            st.warning("For the given parameters, there are no suitable crops available. Please adjust the input values for better recommendations.")

elif option == "Fertilizer Recommendation":
    st.header("Fertilizer Recommendation")
    crop_type = st.selectbox('Select Crop Type', le_crop.classes_)
    soil_type = st.selectbox('Select Soil Type', le_soil.classes_)
    nitrogen = st.number_input('Enter Nitrogen (in Kg/ha)', min_value=0.0)
    phosphorus = st.number_input('Enter Phosphorus (in Kg/ha)', min_value=0.0)
    potassium = st.number_input('Enter Potassium (in Kg/ha)', min_value=0.0)

    # Validate inputs
    if st.button("Predict Fertilizer"):
        crop_type_encoded = le_crop.transform([crop_type])[0]
        soil_type_encoded = le_soil.transform([soil_type])[0]
        data = np.array([[soil_type_encoded, crop_type_encoded, nitrogen, phosphorus, potassium]])
        prediction = fertilizer_model.predict(data)
        
        # Mapping dataset fertilizer names to more user-friendly names
        fertilizer_mapping = {
            '20:20:0': 'Balanced NPK 20-20-0',
            '10:26:26': 'High Phosphorus NPK 10-26-26',
            '28:28': 'High Nitrogen NPK 28-28-0',
            '17:17:17': 'Balanced NPK 17-17-17'
        }
        fertilizer_name = fertilizer_mapping.get(prediction[0], prediction[0])
        
        st.subheader("Recommended Fertilizer:")
        st.success(fertilizer_name)

        # Display a warning if no fertilizer is recommended based on the input
        if fertilizer_name == 'Balanced NPK 17-17-17':
            st.warning("For the given parameters, there might be a better-suited fertilizer. Please adjust the input values for optimized recommendations.")

elif option == "Input References":
    st.sidebar.header("Input Ranges Reference")
    st.sidebar.markdown("""
    ### Nitrogen (N)
    - Low: < 240 Kg/ha
    - Medium: 240 - 480 Kg/ha
    - High: > 480 Kg/ha

    ### Phosphorus (P)
    - Low: < 11 Kg/ha
    - Medium: 11 - 22 Kg/ha
    - High: > 22 Kg/ha

    ### Potassium (K)
    - Low: < 110 Kg/ha
    - Medium: 110 - 280 Kg/ha
    - High: > 280 Kg/ha

    ### pH
    - Acidic: < 6.0
    - Normal to Saline: 6.0 to 8.5
    - Tending to become Alkaline: 8.6 to 9.0
    - Alkaline: > 9.0

    ### Temperature (°C)
    - Low: < 15°C
    - Medium: 15 - 30°C
    - High: > 35°C

    ### Humidity (%)
    - Low: < 40%
    - Medium: 40 - 70%
    - High: > 70%

    ### Rainfall (mm/year)
    - Low: < 500 mm
    - Medium: 500 - 1500 mm
    - High: > 1500 mm
    """)

elif option == "Suggestions":
    st.sidebar.header("Suggestions")
    st.sidebar.markdown("""
    Suggestions for optimizing input values:
    
    1. For high Nitrogen levels, consider planting leguminous crops or using organic manure.
    2. For high Phosphorus levels, avoid phosphorus-rich fertilizers.
    3. For high Potassium levels, use crops that uptake high potassium.
    4. To increase pH in acidic soils, use lime.
    5. To decrease pH in alkaline soils, use sulfur or organic compost.
    6. For low temperatures, consider greenhouse farming to regulate temperature.
    7. For high temperatures, ensure adequate irrigation and mulching to protect crops.
    8. For low humidity, use irrigation to increase humidity.
    9. For high humidity, ensure proper ventilation to reduce fungal diseases.
    10. For low rainfall, use drought-resistant crops or irrigation.
    11. For high rainfall, ensure proper drainage to prevent waterlogging.
    """)

