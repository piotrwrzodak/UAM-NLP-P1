import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import explained_variance_score
from sklearn.metrics import max_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_log_error
from sklearn.metrics import median_absolute_error
from sklearn.metrics import r2_score
from sklearn import preprocessing


def train_model():
    df = pd.read_csv('data/formatted_data.csv')

    le = preprocessing.LabelEncoder()
    balance_data = df.apply(le.fit_transform)

    X = balance_data.drop(columns=['salary', 'street', 'address_text', 'company_url', 'latitude', 'longitude',
                                   'published_at', 'id', 'company_logo_url'])
    y = balance_data['salary']

    model = DecisionTreeClassifier()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model.fit(X_train, y_train)
    # model.fit(X_test, y_test)

    predictions = model.predict(X_test)

    print(explained_variance_score(y_test, predictions))  # 1
    # max_error - a metric that captures the worst case error between the predicted value and the true value, best: 0
    print(max_error(y_test, predictions))
    print(mean_absolute_error(y_test, predictions))
    print(mean_squared_log_error(y_test, predictions))
    # median_absolute_error -  The loss is calculated by taking the median of all absolute differences between the
    # target and the prediction.
    print(median_absolute_error(y_test, predictions))
    print(r2_score(y_test, predictions))



