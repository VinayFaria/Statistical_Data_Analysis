"""
@author: vinay
hypothesis function: h(x) = theta_0 + theta_1*x_1 
"""

import pandas as pd
import numpy as np
from scipy.stats import pearsonr
import matplotlib.pylab as plt
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

df1 = pd.read_csv(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\tutorial_4\abalone_train.csv')
df2 = pd.read_csv(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\tutorial_4\abalone_test.csv')

pearson_coeff = {}
for column in df1:
    if column != 'Rings': # same column pearson coeffient is 1 and highest
        corr, _ = pearsonr(df1[column], df1['Rings'])
        pearson_coeff[column] = corr

Keymax = max(pearson_coeff, key= lambda x: pearson_coeff[x])

dummy_1 = df1[['Rings']].to_numpy()
dummy_1 = dummy_1.reshape(-1, 1)
dummy_2 = df1[[Keymax]].to_numpy()
dummy_2 = dummy_2.reshape(-1, 1)

# training the model
model = LinearRegression().fit(dummy_2, dummy_1)

dummy_3 = df2[[Keymax]].to_numpy()
dummy_3 = dummy_3.reshape(-1, 1)
y_pred_train = model.predict(dummy_2)
y_pred_test = model.predict(dummy_3)
rmse_train = mean_squared_error(df1['Rings'], y_pred_train, squared=False) # Setting squared to False will return the RMSE.
rmse_test = mean_squared_error(df2['Rings'], y_pred_test, squared=False)
print("===== Using Sci-kit learn =====")
print("RMSE on training data is:", rmse_train)
print("RMSE on testing data is:", rmse_test)

plt.figure()
plt.scatter(dummy_2, dummy_1)
plt.scatter(dummy_3, y_pred_test)

#Defining the class
class LinearRegression:
    def __init__(self, x , y):
        self.data = x
        self.target = y
        self.m = 0
        self.b = 0
        self.n = len(x)
         
    def fit(self , epochs , lr):
        
        #Implementing Gradient Descent
        for i in range(epochs):
            y_pred = self.m * self.data + self.b
            
            rmse_coeff = (sum((self.target - y_pred)**2)/self.n)**0.5
            #Calculating derivatives w.r.t Parameters
            D_m = (-2/(2*self.n*rmse_coeff))*np.sum(self.data * (self.target - y_pred))
            D_b = (-1/(2*self.n*rmse_coeff))*np.sum(self.target-y_pred)

            #Updating Parameters
            self.m = self.m - lr * D_m
            self.b = self.b - lr * D_b
             
    def predict(self , inp):
        y_pred = self.m * inp + self.b
        return y_pred
 
#Creating the class object
regressor = LinearRegression(dummy_2, dummy_1)
 
#Training the model with .fit method
regressor.fit(20000 , 0.01) # epochs-100 , learning_rate - 0.001

#Prediciting the values
y_pred_train = regressor.predict(dummy_2)
y_pred_test = regressor.predict(dummy_3)
rmse_train = mean_squared_error(df1['Rings'], y_pred_train, squared=False) # Setting squared to False will return the RMSE.
rmse_test = mean_squared_error(df2['Rings'], y_pred_test, squared=False)
print("===== using linear regression formulas =====")
print("RMSE on training data is:", rmse_train)
print("RMSE on testing data is:", rmse_test)

plt.scatter(dummy_3, y_pred_test)