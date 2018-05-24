Project: Predicting Bike Rentals

Many American cities have communal bike sharing stations where you can rent bicycles by the hour or day. Washington, D.C. is one of these cities. The District collects detailed data on the number of bicycles people rent by the hour and day.

The file contains 17380 rows, with each row representing the number of bike rentals for a single hour of a single day.

In this project, I'll try to predict the total number of bikes people rented in a given hour. I'll predict the cnt column using all of the other columns, except for casual and registered.

To take a look at the distribution of total rentals, a histogram of the cnt column of bike_rentals was made. Using the corr method on the bike_rentals dataframe, I explored how each column is correlated with cnt.

The data was split into into training and testing sets to train an algorithm using the training set, and evaluate its accuracy on the testing set.

Now that some exploration and manipulation, I applied linear regression to the data. But, linear regression is prone to underfitting the data and may not build a powerful enough model. So alternatively I applied the decision tree algorithm because then I'll be able to compare its error with the error from linear regression. This will enable me to pick the right algorithm for this data set. I also applied the random forest algorithm, which improves on the decision tree algorithm. Random forests tend to be much more accurate than simple models like linear regression. Due to the way random forests are constructed, they tend to overfit much less than decision trees. Random forests can still be prone to overfitting, though, so it's important to tune parameters like maximum depth and minimum samples per leaf. I used RandomForestRegressor class from sklearn.ensemble to fit a random forest algorithm to the train data.

In the end, we will observe that by removing some of the sources of overfitting, the random forest accuracy is improved over the decision tree accuracy.
