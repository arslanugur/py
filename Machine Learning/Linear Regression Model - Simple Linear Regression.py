# 1. Load the required library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline


# 2. Prepare data and view top 5 record
data = {"YearsExperience': [ 1.1, 1.3, 1.5, 2., 2.2, 2.9, 3., 3.2, 3.2, 3.7, 3.9,
        4., 4., 4.1, 4.5, 4.9, 5.1, 5.3, 3.9, 6., 6.8, 7.1,
        7.9, 8.2, 8.7, 9., 9.5, 9.6, 10.3, 10.5],
        "Salary":[39343.,46285., 37731., 43525., 39891., 56642., 60150.,
                  56445., 64645., 57189., 63218., 55794., 30957., 57081.,
                  61111., 67938., 66029., 83088., 81363., 93940., 91738.,
                  98273., 101302., 113812., 109431., 195582., 116969., 112635.,
                  122391., 121872.))
dataframe = pd.DataFrame(data)
dataframe.head()

# 3. Split the features and target variable
x = dataframe.iloc[:,0].values.reshape(-1,1)
y = dataframe.iloc[:,1].values.reshape(-1,1)

# 4.Plot the Scatter diagram of the dataset
plt.scatter(x,y)
plt.title("Year of Experience vs Salary")
plt.xlabel("Year of Experience")
plt.ylabel("Salary")
plt.show()


# 5. Split data in train test
from sklearn.model_selection import train_test_split
x train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.30, random_state=0)

# 6. Create the model, train and predict with test data
from sklearn.linear_model import LinearRegression
linearregression = LinearRegression()
linearregression.fit(x_train,y_train)
y_predict = linearregression.predict(x_test)

# 7. Visualize in grpah
x_min,x_max = dataframe.YearsExperience.min(), dataframe.YearsExperience.max()
x_new = pd.DataFrame({'YearsExperience': [x_min, x_max]})
x_predicted = linearregression.predict(x_new)
dataframe.plot(kind='scatter',x='YearsExperience',y='Salary')
plt.plot(x_new,x_predicted,c='red',linewidth=2)





