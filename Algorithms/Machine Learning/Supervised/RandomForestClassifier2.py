#Import Library
from sklearn.ensemble import RandomForestClassifier
#Assumed u have, X (predictor), and Y (target) for
#training data set and x_test(predictor) of test_dataset
#Create Random Forest Object
model = RandomForestClassifier()
#Train the model using the training sets and check score
model.fit(X, Y)
#Predict Output
predicted = model.predict(x_test)
