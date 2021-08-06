import numpy as np
import streamlit as st
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_squared_log_error as msle


def app(data_df):

    cars_df = data_df

    X = cars_df.loc[:, cars_df.columns[:-1]]
    y = cars_df['price']

    lr = LinearRegression().fit(X, y)

    y_pred = lr.predict(X)

    st.header("Data Prediction")

    X_input = [[]]

    st.subheader("Enter various specifications of car")

    X_input[0].append(
        st.slider(
            "Enter value for Car Width",
            min_value=float(cars_df['carwidth'].min()),
            max_value=float(cars_df['carwidth'].max()),
        ))

    X_input[0].append(
        st.slider("Enter value for Engine SIze",
                  min_value=float(cars_df['enginesize'].min()),
                  max_value=float(cars_df['enginesize'].max())))

    X_input[0].append(
        st.slider("Enter value for Horse Power",
                  min_value=float(cars_df['horsepower'].min()),
                  max_value=float(cars_df['horsepower'].max())))

    if st.checkbox("Is drive wheel forward?"):
        X_input[0].append(1)

    else:
        X_input[0].append(0)

    if st.checkbox("Is Car Comapny Buik"):
        X_input[0].append(1)

    else:
        X_input[0].append(0)

    def predict():
        st.subheader("Prediction")
        st.write(
            f"The predicted price of car is: {lr.predict(X_input)[0]:,.2f} rupees"
        )
        st.write(
            f"The mean of Absolute errors in prediction of model is: {mae(y, y_pred):,.2f} rupees"
        )
        st.write(
            f"The mean of Square of errors of in prediction  of model is: {mse(y, y_pred):,.2f} rupees"
        )
        st.write(
            f"The Root of mean of Square of errors of in prediction  of model is: {np.sqrt(mse(y, y_pred)):,.2f}"
        )
        st.write(
            f"The mean of Square of log of errors of in prediction  of model is: {msle(y, y_pred):0.2f}"
        )

        st.write(f"R2 score of the model is: {r2_score(y, y_pred):.2f}")

    if st.button("Predict"):
        predict()