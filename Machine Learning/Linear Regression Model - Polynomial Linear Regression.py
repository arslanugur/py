# 1.Import required library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# 2.Load dataset and view top 5 record
data = {"Level" :[1, 2, 3, 4, 5, 6, 7, 8, 9, 101, "Salary :[  45000, 50000, 50000, 80000, 110000, 150000, 200000, 300000, 500000, 1000000]}
df pd.Datafrane(data)
df.head()
                  
# 3. Select the features and target variable
x = df.iloc[:,0:1].values
y = df.iloc [:,1].values
# Now here we create the model with both Simple Linear regression
# and Polynomial Regression model and compare the result
#First we create the model using linear regression

# 4. Create the model for simple linear regression model

                  
# 5.create the model using polynomial regression for that 
# first we convert the features into polynomial of degree 4 and create the model and train with train data
poly = PolynomialFeatures(degree=4)
x_poly = poly.fit_transform(x)
poly_line = LinearRegression()
poly_line.fit(x_poly,y)

# 6. Check the predict of simple linear regression using graph
plt.scatter(x,y)
plt.plot(x, linearregression.predict(x))

# 6. Check the predict of polynomial regression using graph
plt.scatter(x,y)
plt.plot(x,poly_line.predict(poly.fit_transform(x)))


