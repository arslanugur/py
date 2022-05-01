# 1.Import required library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


# 2.Load dataset and view top 5 record
df = pd.read_csv('Advertising.csv')
df.head()


# 2.Draw the scatter diagram of each independent varaible and target variable
fig, axs = plt.subplots(1,3)
df.plot(kind='scatter',x='TV', y='sales', figsize=(16,6),ax=axs[0])
df.plot(kind='scatter',x='radio',y='sales', figsize=(16,6),ax=axs[1])
df.plot(kind='scatter',x='newspaper',y='sales',figsize=(16,6),ax=axs[2])
plt.show()


# 3. Select the features and split into dependent and independent variable
feature_cols = ['TV', 'radio', 'newspaper']
X = df[feature_cols]
Y= df.sales


# 4.Split data into train-test, load model and train model with train data
xtrain, xtest, ytrain,ytest = train_test_split(X,Y,test_size=0.30)
lm = LinearRegression()
lm.fit(xtrain, ytrain)

# 5. Test the model with test data and check the intercept, coefficient and MSE of model
p=lm.predict(xtest)
print(lm.intercept_)
print(lm.coef_)
print(mean_squared_error(ytest,p))

# Dataset Source: https://www.kaggle.com/ashydv/advertising-dataset




