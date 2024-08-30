import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import joblib
from data_preprocessing import preprocess_data

def train_crop_recommendation_model(crop_data):
    X = crop_data[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
    y = crop_data['label']
    model = RandomForestClassifier(n_estimators=200, random_state=42)
    
    # Hyperparameter tuning
    param_grid = {
        'n_estimators': [100, 200, 300],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }
    
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=3, n_jobs=-1, verbose=2)
    grid_search.fit(X, y)
    
    return grid_search.best_estimator_

def train_fertilizer_recommendation_model(fertilizer_data):
    fertilizer_data.columns = fertilizer_data.columns.str.strip()
    
    X = fertilizer_data[['Soil Type', 'Crop Type', 'Nitrogen', 'Phosphorous', 'Potassium']]
    y = fertilizer_data['Fertilizer Name']
    model = RandomForestClassifier(n_estimators=200, random_state=42)
    
    # Hyperparameter tuning
    param_grid = {
        'n_estimators': [100, 200, 300],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }
    
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=3, n_jobs=-1, verbose=2)
    grid_search.fit(X, y)
    
    return grid_search.best_estimator_

if __name__ == "__main__":
    crop_data, fertilizer_data, le_crop, le_soil = preprocess_data()
    crop_model = train_crop_recommendation_model(crop_data)
    fertilizer_model = train_fertilizer_recommendation_model(fertilizer_data)

    # Save the models
    joblib.dump(crop_model, 'crop_model.pkl')
    joblib.dump(fertilizer_model, 'fertilizer_model.pkl')
