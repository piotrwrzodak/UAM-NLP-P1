import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import BayesianRidge

from sklearn.model_selection import train_test_split
from sklearn.metrics import explained_variance_score
from sklearn.metrics import max_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_log_error
from sklearn.metrics import median_absolute_error
from sklearn.metrics import r2_score
from sklearn import preprocessing


def split_data():
    df = pd.read_csv('data/formatted_data.csv')

    le = preprocessing.LabelEncoder()
    data = df.apply(le.fit_transform)

    X = data.drop(columns=['salary', 'street', 'address_text', 'company_url', 'latitude', 'longitude',
                           'published_at', 'id', 'company_logo_url', 'remote_interview'])
    y = data['salary']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    return X_train, X_test, y_train, y_test


def decision_tree_classifier(X_train, X_test, y_train, y_test):
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    test_accuracy('DecisionTreeClassifier', predictions, y_test)


def linear_regression(X_train, X_test, y_train, y_test):
    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    test_accuracy('LinearRegression', predictions, y_test)


def decision_tree_regressor(X_train, X_test, y_train, y_test):
    model = DecisionTreeRegressor(random_state=0)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    test_accuracy('DecisionTreeRegressor', predictions, y_test)


def bayesian_ridge(X_train, X_test, y_train, y_test):
    model = BayesianRidge()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    test_accuracy('BayesianRidgeRegression', predictions, y_test)


def train_model():
    X_train, X_test, y_train, y_test = split_data()
    decision_tree_classifier(X_train, X_test, y_train, y_test)
    linear_regression(X_train, X_test, y_train, y_test)
    decision_tree_regressor(X_train, X_test, y_train, y_test)
    bayesian_ridge(X_train, X_test, y_train, y_test)


def test_accuracy(name, predictions, y_test):
    print('\n', name, 'accuracy:')

    print('explained_variance_score', explained_variance_score(y_test, predictions))  # best: 1

    # max_error - a metric that captures the worst case error between the predicted value and the true value, best: 0
    print('max_error', max_error(y_test, predictions))

    print('mean_absolute_error', mean_absolute_error(y_test, predictions))

    # median_absolute_error -  The loss is calculated by taking the median of all absolute differences between the
    # target and the prediction.
    print('median_absolute_error', median_absolute_error(y_test, predictions))

    print('r2_score', r2_score(y_test, predictions))
