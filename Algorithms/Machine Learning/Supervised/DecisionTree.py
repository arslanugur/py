#import library
#import other necessary libraries like pandas, numpy..
from sklearn import tree
#assumed u have, x (predictor) and y (target) for training data set and x_test(predictor) of test_dataset

#create tree object
model = tree.DecisionTreeClassifier(criterion = 'gini')
#for classification, here u can change the algorithms as gini or entropy (information gain) by default it is gini
#model = tree.DecisionTreeRegressor() for regression
#train the model using the training sets and check score
model.fit(x, y)
model.score(x, y)
#predict output
predicted = model.predict(x_test)
