"""
CatBoost is a recently open-sourced machine learning algorithm from Yandex. 
It can easily integrate with deep learning frameworks like Google’s TensorFlow and Apple’s Core ML.
The best part about CatBoost is that it does not require extensive data training like other ML models, 
and can work on a variety of data formats; not undermining how robust it can be.
Make sure you handle missing data well before you proceed with the implementation.
Catboost can automatically deal with categorical variables without showing the type conversion error, 
which helps you to focus on tuning your model better rather than sorting out trivial errors.
"""

import pandas as pd
import numpy as np

from catboost import CatBoostRegressor

#Read training and testing files
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

#Imputing missing values for both train and test
train.fillna(-999, inplace=True)
test.fillna(-999,inplace=True)

#Creating a training set for modeling and validation set to check model performance
X = train.drop(['Item_Outlet_Sales'], axis=1)
y = train.Item_Outlet_Sales

from sklearn.model_selection import train_test_split

X_train, X_validation, y_train, y_validation = train_test_split(X, y, train_size=0.7, random_state=1234)
categorical_features_indices = np.where(X.dtypes != np.float)[0]

#importing library and building model
from catboost import CatBoostRegressormodel=CatBoostRegressor(iterations=50, depth=3, learning_rate=0.1, loss_function='RMSE')

model.fit(X_train, y_train,cat_features=categorical_features_indices,eval_set=(X_validation, y_validation),plot=True)

submission = pd.DataFrame()

submission['Item_Identifier'] = test['Item_Identifier']
submission['Outlet_Identifier'] = test['Outlet_Identifier']
submission['Item_Outlet_Sales'] = model.predict(test)

#https://www.analyticsvidhya.com/blog/2017/08/catboost-automated-categorical-data/
