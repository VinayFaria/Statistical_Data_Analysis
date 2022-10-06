"""
@author: vinay
"""

import pandas as pd

df = pd.read_excel(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\Data\climate\annual_max_temp_1901_2017_NWH_cru_0.25x0.25.xlsx')
UP_dataframe = df[["X7929"]]
dummy_1 = UP_dataframe.loc[UP_dataframe["X7929"].between(38.5, 39)]

HP_dataframe = df[["X77.2530.5"]]
dummy_2 = HP_dataframe.loc[HP_dataframe["X77.2530.5"].between(38.5, 39)]

print("Temperature observations between 38.5 to 39 degree Celsius in UP: ", dummy_1[dummy_1.columns[0]].count())
print("Temperature observations between 38.5 to 39 degree Celsius in HP: ", dummy_2[dummy_2.columns[0]].count())