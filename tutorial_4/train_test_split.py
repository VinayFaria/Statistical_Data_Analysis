"""
@author: vinay
"""

import pandas as pd
from sklearn.model_selection import train_test_split
housing = pd.read_csv(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\Data\abalone.csv')

#splitting
x_train, x_test=train_test_split(housing, test_size=0.3)
x_train.to_csv(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\tutorial_4\abalone_train.csv', index = False)
x_test.to_csv(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\tutorial_4\abalone_test.csv', index = False)