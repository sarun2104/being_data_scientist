import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import RFECV
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

test = pd.read_csv(r"C:\Users\sarun\Downloads\Kaggle Project\test.csv")
print(test.shape)

train = pd.read_csv(r"C:\Users\sarun\Downloads\Kaggle Project\train.csv")
print(train.shape)

# Preprocessing the Data

def process_missing(df):
    df["Fare"] = df["Fare"].fillna(train["Fare"].mean())
    df["Embarked"] = df["Embarked"].fillna("S")
    return df

"""
The age column in the dataframe is a continuous feature.
It is necessary to separate this continuous feature into a categorical feature by dividing it into ranges.
I used the pandas.cut() function for this.
"""

def process_age(df):
    df["Age"] = df["Age"].fillna(-0.5)
    cut_points = [-1, 0, 5, 12, 18, 35, 60, 100]
    label_names = ["Missing", "Infant", "Child", "Teenager", "Young Adult", "Adult", "Senior"]
    df["Age_categories"] = pd.cut(df["Age"], cut_points, labels=label_names)
    return df

def create_dummies(df,column_name):
    dummies = pd.get_dummies(df[column_name], prefix=column_name)
    df = pd.concat([df, dummies], axis=1)
    return df

def process_fare(df):
    cut_points = [-1, 12, 50, 100, 1000]
    label_names = ["0-12", "12-50", "50-100", "100+"]
    df["Fare_categories"] = pd.cut(df["Fare"], cut_points, labels=label_names)
    return df

def process_cabin(df):
    df["Cabin_type"] = df["Cabin"].str[0]
    df["Cabin_type"] = df["Cabin_type"].fillna("Unknown")
    df = df.drop('Cabin', axis=1)
    return df

def process_titles(df):
    titles = {
        "Mr": "Mr",
        "Mme": "Mrs",
        "Ms": "Mrs",
        "Mrs": "Mrs",
        "Master": "Master",
        "Mlle": "Miss",
        "Miss": "Miss",
        "Capt": "Officer",
        "Col": "Officer",
        "Major": "Officer",
        "Dr": "Officer",
        "Rev": "Officer",
        "Jonkheer": "Royalty",
        "Don": "Royalty",
        "Sir": "Royalty",
        "Countess": "Royalty",
        "Dona": "Royalty",
        "Lady": "Royalty"
    }
    extracted_titles = df["Name"].str.extract(' ([A-Za-z]+)\.', expand=False)
    df["Title"] = extracted_titles.map(titles)
    return df


def pre_process(df):
    df = process_missing(df)
    df = process_age(df)
    df = process_fare(df)
    df = process_titles(df)
    df = process_cabin(df)

    for col in ["Age_categories", "Fare_categories",
                "Title", "Cabin_type", "Sex"]:
        df = create_dummies(df, col)

    return df


train = pre_process(train)
test = pre_process(test)

def process_isalone(df):
    df["familysize"] = df[["SibSp","Parch"]].sum(axis=1)
    df["isalone"] = 0
    df.loc[(df["familysize"] == 0),"isalone"] = 1
    df = df.drop("familysize",axis=1)
    return df

train = process_isalone(train)
test = process_isalone(test)

def select_features(df):
    df = df.select_dtypes([np.number]).dropna(axis=1)
    all_X = df.drop(["Survived", "PassengerId"], axis=1)
    all_y = df["Survived"]

    clf = RandomForestClassifier(random_state=1)
    selector = RFECV(clf, cv=10)
    selector.fit(all_X, all_y)

    best_columns = list(all_X.columns[selector.support_])
    print("Best Columns \n" + "-" * 12 + "\n{}\n".format(best_columns))

    return best_columns


cols = select_features(train)

def select_model(df, features):
    all_X = df[features]
    all_y = df["Survived"]

    # List of dictionaries, each containing a model name,
    # it's estimator and a dict of hyperparameters
    models = [
        {
            "name": "LogisticRegression",
            "estimator": LogisticRegression(),
            "hyperparameters":
                {
                    "solver": ["newton-cg", "lbfgs", "liblinear"]
                }
        },
        {
            "name": "KNeighborsClassifier",
            "estimator": KNeighborsClassifier(),
            "hyperparameters":
                {
                    "n_neighbors": range(1, 20, 2),
                    "weights": ["distance", "uniform"],
                    "algorithm": ["ball_tree", "kd_tree", "brute"],
                    "p": [1, 2]
                }
        },
        {
            "name": "RandomForestClassifier",
            "estimator": RandomForestClassifier(random_state=1),
            "hyperparameters":
                {
                    "n_estimators": [4, 6, 9],
                    "criterion": ["entropy", "gini"],
                    "max_depth": [2, 5, 10],
                    "max_features": ["log2", "sqrt"],
                    "min_samples_leaf": [1, 5, 8],
                    "min_samples_split": [2, 3, 5]

                }
        }
    ]

    for model in models:
        print(model['name'])
        print('-' * len(model['name']))

        grid = GridSearchCV(model["estimator"],
                            param_grid=model["hyperparameters"],
                            cv=10)
        grid.fit(all_X, all_y)
        model["best_params"] = grid.best_params_
        model["best_score"] = grid.best_score_
        model["best_model"] = grid.best_estimator_

        print("Best Score: {}".format(model["best_score"]))
        print("Best Parameters: {}\n".format(model["best_params"]))

    return models


result = select_model(train, cols)


def save_submission_file(model, cols, filename="submission.csv"):
    holdout_data = test[cols]
    predictions = model.predict(holdout_data)

    holdout_ids = test["PassengerId"]
    submission_df = {"PassengerId": holdout_ids,
                     "Survived": predictions}
    submission = pd.DataFrame(submission_df)

    submission.to_csv(filename, index=False)


best_rf_model = result[2]["best_model"]
save_submission_file(best_rf_model, cols)