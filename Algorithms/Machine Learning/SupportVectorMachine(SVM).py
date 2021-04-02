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
