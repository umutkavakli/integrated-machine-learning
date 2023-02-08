import pandas as pd
import joblib

class ModelLoader:

    __models = {
        'Linear Regression': 'linear',
        'Decision Tree Regressor': 'decision_tree',
        'Random Forest Regressor': 'random_forest',
        'XGBoost Regressor': 'xgboost',
        'SVM Regressor': 'svm',
        'KNN': 'knn'
    }

    def __init__(self, model='Linear Regression'):
        self.model = joblib.load(f'models/{ModelLoader.__models[model]}.pkl')
        self.model_name = ModelLoader.__models[model]
        
    def set_model(self, model):
        self.model = joblib.load(f'models/{ModelLoader.__models[model]}.pkl')

    def get_model(self):
        return self.model_name

    def get_feature_names(self):
        features = ['sheet-thickness', 'yield-strength', 'tensile-strength', 'mold-weight']
        return self.data[features]

    def get_target(self):
        target = 'cost'
        return self.data[target]
