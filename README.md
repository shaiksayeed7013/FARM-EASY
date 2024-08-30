# FARM-EASY


## Overview
FARM EASY is a Streamlit-based application designed to assist farmers with crop and fertilizer recommendations based on specific environmental and soil conditions. The application uses machine learning models to predict the most suitable crop and fertilizer for a given set of inputs, thereby aiding in optimizing agricultural yield and sustainability.

## Features
- **Crop Recommendation:** Predicts the best crop to plant based on nitrogen, phosphorus, potassium levels, temperature, humidity, pH, and rainfall.
- **Fertilizer Recommendation:** Suggests the optimal fertilizer based on soil type, crop type, and levels of nitrogen, phosphorus, and potassium.
- **Input Validation:** Provides warnings if the input values are outside the optimal range and suggests adjustments.
- **User-Friendly Interface:** Easy navigation through different sections like Home, Crop Recommendation, Fertilizer Recommendation, Input References, and Suggestions.

## Dataset
- **crop_recommendation.csv:** Contains data for crop recommendations based on environmental and soil parameters.
- **Fertilizer Prediction.csv:** Contains data for fertilizer recommendations based on soil type, crop type, and nutrient levels.

## Installation
### Clone the Repository
```bash
git clone https://github.com/your-username/FARM-EASY.git
cd FARM-EASY
```

### Run the Application
### Installation and Setup

1. **Create a Virtual Environment (optional but recommended):**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

2. **Install the Required Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Data Preprocessing Script:**

```bash
python data_preprocess1.py
```
4. **Train the Models :**

```bash
python model1.py
```
5. **Launch the Streamlit Application:**

```bash
streamlit run main1.py
```

### Crop Recommendation
- Navigate to the **Crop Recommendation** section.
- Input values for Nitrogen (N), Phosphorus (P), Potassium (K), Temperature, Humidity, pH, and Rainfall.
- Click **Predict Crop** to get the recommended crop based on the provided inputs.
- If any values are out of the optimal range, the app will provide warnings and suggest possible corrections.

### Fertilizer Recommendation
- Navigate to the **Fertilizer Recommendation** section.
- Select the Crop Type and Soil Type from the dropdown menus.
- Input values for Nitrogen, Phosphorus, and Potassium.
- Click **Predict Fertilizer** to get the recommended fertilizer based on the provided inputs.
- The app will map the prediction to a more user-friendly name and display it.

### Input References
- Provides a reference guide for the ranges of input values like Nitrogen, Phosphorus, Potassium, pH, Temperature, Humidity, and Rainfall.
- Helps users to understand the input ranges and their implications.

### Suggestions
- Offers suggestions for optimizing input values based on agricultural best practices.
- Useful for fine-tuning inputs for better crop and fertilizer recommendations.

### Model Training
The models for crop and fertilizer recommendations were trained using `RandomForestClassifier` with hyperparameter tuning via `GridSearchCV`.

### Training the Models
1. Preprocess the data using `data_preprocess1.py`.
   ```bash
   python data_preprocess1.py
   ```
2.  Train the models using `model1.py`.
  ```bash
python model1.py
  ```
3. The trained models will be saved as crop_model.pkl and fertilizer_model.pkl.


### Sample Output

#### Crop Recommendation
```plaintext
Recommended Crop: Rice
```
#### Fertilizer Recommendation
```plaintext
Recommended Fertilizer: Balanced NPK 20-20-0
```

### Future Work
- **Advanced Models**: Explore more advanced machine learning models or deep learning techniques for improved accuracy.
- **Hyperparameter Tuning**: Further fine-tuning of model hyperparameters for better performance.
- **Extended Dataset**: Incorporate additional datasets to enhance the model's predictive power.
- **Real-time Data**: Integrate real-time weather and soil data to provide more accurate recommendations.

### Acknowledgements
- **Datasets**: The datasets used for training the models were sourced from reliable agricultural resources.
- **Libraries**: The project was made possible using Python libraries like pandas, scikit-learn, joblib, and streamlit.
- **Contributors**: Thanks to all contributors who helped in the development and testing of this application.

### Useful Links
- [Streamlit Documentation](https://docs.streamlit.io/)
- [scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [GitHub Repository](https://github.com/your-username/FARM-EASY)

