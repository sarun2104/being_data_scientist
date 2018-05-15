Project: Predicting House Sale Prices using Linear Regression

The dataset we will be working with is the housing data for the city of Ames, Iowa, United States from 2006 to 2010.

The project started by creating a function train_and_test() which separates the training and testing section of the dataframe. Then I moved to feature engineering by removing features with many missing values, diving deeper into potential categorical features, and transforming text and numerical columns.

A transform_features() function is created next. In general, the goal of this function is to remove features that we don't want to use in the model, just based on the number of missing values or data leakage and transform features into the proper format (numerical to categorical, scaling numerical, filling in missing values, etc). Finally this function create new features by combining other features.

The next step is feature selection. Feature selection is done by generating a correlation heatmap matrix of the numerical features in the training data set. Then calculate the correlation coefficients for the columns that seem to correlate well with SalePrice. Because we have a pipeline in place, it's easy to try different features and see which features result in a better cross validation score.

Now the final part of the pipeline is training and testing. When iterating on different features, using simple validation is a good idea. I  added a new parameter named k to train_and_test function that controls the type of cross validation that occurs.

