"""
@author: vinay
"""

import pandas as pd

X = [102, 105, 112, 103, 117, 110, 122] # Duration
Y = [12032, 12405, 12903, 10853, 11738, 12361, 13134] # Volume

df = pd.DataFrame(list(zip(X, Y)), columns =['Duration', 'Volume'])

mean_Duration = df["Duration"].mean()
mean_Volume = df["Volume"].mean()

dummy1 = 0
dummy2 = 0

for ind in df.index:
    dummy1 += (df['Duration'][ind] - mean_Duration)*(df['Volume'][ind] - mean_Volume)
    dummy2 += (df['Duration'][ind] - mean_Duration)*(df['Duration'][ind] - mean_Duration)

beta_1 = dummy1/dummy2

beta_0 = mean_Volume - beta_1*mean_Duration

user_input = input("Give the value of flood duration for which you want to find flood volume: ")
try:
    number = int(user_input)
except ValueError:
    number = float(user_input)

flood_volume = beta_0 + beta_1*number
print("Flood volume is", flood_volume)
