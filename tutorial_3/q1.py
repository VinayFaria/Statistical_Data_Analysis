"""
@author: Vinay
Question: Load the NWH temperature dataset and calculate the means of the first ten columns. What is the maximum mean temperature value?
Dataset: NWH_temp_data_25_1901_2017_cru_data
"""

import pandas as pd

df = pd.read_csv(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\Data\climate\NWH_temp_data_25_1901_2017_cru_data.csv')
mean_list = []
count = 0
for column in df:
    mean_list.append(df[column].mean())
    count += 1
    if count == 10:
        break

print("Maximum temperature is", max(mean_list))