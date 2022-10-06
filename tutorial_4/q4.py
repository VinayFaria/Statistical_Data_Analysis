"""
@author: vinay
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

df1 = pd.read_csv(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\tutorial_4\abalone_train.csv')
df2 = pd.read_csv(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\tutorial_4\abalone_test.csv')
polynomial = []
rmse_test_list = []
for i in range(1,6):
    poly_features = PolynomialFeatures(degree = i, include_bias = False)
    x_poly = poly_features.fit_transform(df1.loc[:, df1.columns != 'Rings'].to_numpy())
    
    lin_reg = LinearRegression()
    lin_reg.fit(x_poly, df1[['Rings']].to_numpy())
    
    x_new_poly = poly_features.transform(df2.loc[:, df1.columns != 'Rings'].to_numpy())
    y_pred_train = lin_reg.predict(x_poly)
    y_pred_test = lin_reg.predict(x_new_poly)
    
    rmse_train = mean_squared_error(df1['Rings'], y_pred_train, squared=False) # Setting squared to False will return the RMSE.
    rmse_test = mean_squared_error(df2['Rings'], y_pred_test, squared=False)
    print("===== Using Sci-kit learn =====")
    print("RMSE on training data for degree",i,"is:", rmse_train)
    print("RMSE on testing data",i," is:", rmse_test)
    polynomial.append(i)
    rmse_test_list.append(rmse_test)

plt.bar(polynomial, rmse_test_list)
plt.xlabel("Order of polynomial")
plt.ylabel("RMSE value")
plt.title("RMSE vs order of polynomial")
for i,j in zip(polynomial, rmse_test_list):
    plt.text(i, j, j)
plt.show()