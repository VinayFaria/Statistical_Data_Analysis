"""
@author: vinay
hypothesis function: h(x) = theta_0 + theta_1 * x_1 + theta_2 * x_2 .....theat_n * x_n
"""

import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

df1 = pd.read_csv(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\tutorial_4\abalone_train.csv')
df2 = pd.read_csv(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\tutorial_4\abalone_test.csv')

dummy_1 = df1[['Rings']].to_numpy()
dummy_2 = df1.loc[:, df1.columns != 'Rings'].to_numpy()

# training the model
model = LinearRegression().fit(dummy_2, dummy_1.reshape(-1, 1))

dummy_3 = df2.loc[:, df1.columns != 'Rings'].to_numpy()
y_pred_train = model.predict(dummy_2)
y_pred_test = model.predict(dummy_3)
rmse_train = mean_squared_error(df1['Rings'], y_pred_train, squared=False) # Setting squared to False will return the RMSE.
rmse_test = mean_squared_error(df2['Rings'], y_pred_test, squared=False)
print("===== Using Sci-kit learn =====")
print("RMSE on training data is:", rmse_train)
print("RMSE on testing data is:", rmse_test)