import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data():
    # Load datasets
    crop_data = pd.read_csv('crop_recommendation.csv')
    fertilizer_data = pd.read_csv('Fertilizer Prediction.csv')

    # Encode labels for fertilizer prediction
    le_crop = LabelEncoder()
    fertilizer_data['Crop Type'] = le_crop.fit_transform(fertilizer_data['Crop Type'])
    le_soil = LabelEncoder()
    fertilizer_data['Soil Type'] = le_soil.fit_transform(fertilizer_data['Soil Type'])

    return crop_data, fertilizer_data, le_crop, le_soil

if __name__ == "__main__":
    crop_data, fertilizer_data, le_crop, le_soil = preprocess_data()
    # Save the LabelEncoders
    import joblib
    joblib.dump(le_crop, 'le_crop.pkl')
    joblib.dump(le_soil, 'le_soil.pkl')
