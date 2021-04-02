'''
It is a classification method. 
In the algorithm, we plot each data item 
as a point in n-dimensional space (where n is number of features you have) 
with the value of each feature being the value of a particular coordinate.
For example, if we only had two features like Height and Hair length of an individual, 
we’d first plot these two variables in two dimensional space 
where each point has two co-ordinates (these co-ordinates are known as Support Vectors)
'''

#import Library
from sklearn import svm
#Assumed u have, X (predictor) and Y (target) for
#training data set and x_test(predictor) of test_dataset
#Create SVM classificaton object
model = svm.svc()
#there are various options associated with it, this is simple for classification.
#Train the model using the training sets and check
#score
model.fit(x, y)
model.score(x, y)
#Predict Output
predicted = model.predict(x_test)
