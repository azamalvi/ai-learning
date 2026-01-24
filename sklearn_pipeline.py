from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def house_price_prediction_pipeline():
    # data
    X = [[1000], [1500], [2000], [2500], [3000]]
    y = [200000, 250000, 300000, 350000, 400000]

    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    # Create a pipeline
    pipeline = Pipeline([
        ('scaler', StandardScaler()), # step 1: preprocessing
        ('model', LinearRegression()) # step 2: model
    ])

    # Train the model
    pipeline.fit(X_train, y_train)

    # Make predictions
    predictions = pipeline.predict(X_test)
    # print("Predictions:", predictions)
    # Evaluate the model
    # score = pipeline.score(X_test, y_test)
    # print("Model Score:", score)

    # Display actual vs predicted
    for x, actual, pred in zip(X_test, y_test, predictions):
        print(f"input={x} -> actual={actual}, predicted={pred}")

    # new sample prediction
    new_sample = [[1800], [2950], [4000]]
    predicted_price = pipeline.predict(new_sample)

    # Display predictions for new samples
    for x, p in zip(new_sample, predicted_price):
        print(f"input={x} -> predicted={p}")


def preprocessing_house_price_prediction_pipeline(new_sample: list[[int, str]] = None):
    # sample data
    X = [
        [1000, "city"],
        [1500, "city"],
        [1200, "suburb"],
        [1800, "suburb"]
    ]

    y = [100000, 150000, 120000, 180000]

    # feature names
    num_features = [0]   # house size
    cat_features = [1]   # location

    # preprocessing
    preprocessing = ColumnTransformer([
        ("num", StandardScaler(), num_features),
        ("cat", OneHotEncoder(), cat_features)
    ])

    # pipeline
    pipe = Pipeline([
        ("preprocessing", preprocessing),  # step 1
        ("model", LinearRegression())       # step 2
    ])

    # split
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    # train
    pipe.fit(X_train, y_train)

    # predict
    predicted_price = pipe.predict(X_test)
    for x, actual, pred in zip(X_test, y_test, predicted_price):
        print(f"input={x} -> actual={actual}, predicted={pred}")

    new_predict_price = pipe.predict(new_sample)
    for x, p in zip(new_sample, new_predict_price):
        print(f"input={x} -> predicted={p}")

    y_pred = pipe.predict(X_test)
    print("MAE:", mean_absolute_error(y_test, y_pred))
    print("MSE:", mean_squared_error(y_test, y_pred))
    print("R² :", r2_score(y_test, y_pred))


# house_price_prediction_pipeline()
preprocessing_house_price_prediction_pipeline([[3000, "city"], [3000, "suburb"]])