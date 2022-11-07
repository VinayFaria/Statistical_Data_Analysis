"""
@author: Bharat
"""

import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.read_csv(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\Data\map\latlongNWH.csv)
plt.scatter(df1.x, df1.y, color='blue', header=None)
plt.show()

df2 = pd.read_csv(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\Data\climate\NWH-CRU_pre_1901-2020_month_50km.csv', header=None)
df2.columns
plt.scatter(df2.x, df2.y, color='red')
plt.show()

res = pd.merge(df1, df2, how='inner')
res.to_csv(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\Data\climate\NWH-CRU_pre_1901-2020_month_50km_cleaned.csv')

# data cleaning
# result=res.dropna()
# result.to_csv("clean_pre_result.csv")
# plt.scatter(result.x, result.y, color='green')