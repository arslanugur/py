#import library
library(rpart)
x <- cbind(x_train, y_train)
#grow tree
fit <- rpart(y_train ~ ., data = x, method = "class")
summary(fit)
#predict output
predicted = predict(fit, x_test)
