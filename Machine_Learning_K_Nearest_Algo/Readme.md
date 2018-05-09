Project: Predicting Car Prices using K Nearest Neighbor Algorithm

In this guided project, I used the machine learning workflow to predict a car's market price using its attributes. The data set contains information on various cars. For each car we have information about the technical aspects of the vehicle such as the motor's displacement, the weight of the car, the miles per gallon, how fast the car accelerates, and more.

The first step is to determine which columns are numeric and can be used as features and which column is the target column. The next step was to clean the data set by removing missing values and rescaling the values in the numeric columns so they all range from 0 to 1.

In the beginning I used some univariate k-nearest neighbors models. A function, named knn_train_test() was created that encapsulates the training and simple validation process. I used this function to train and test univariate models using the different numeric columns in the data set. Then I modified the knn_train_test() function to create, train, and test a univariate model using the following k values (1, 3, 5, 7, and 9) instead of the default.

In the final step, I modified the knn_train_test() function to work with multiple columns.
