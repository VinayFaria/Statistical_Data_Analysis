"""
@author: Vinay
Question: Plot the shape file of India.
Dataset: Indian_States
"""

import geopandas
import matplotlib.pyplot as plt

#df = pd.read_csv(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\Data\climate\latlongNWH.csv')
#plt.scatter(df.x, df.y, color='red')

NWH = geopandas.read_file("D:/Postgraduation/OneDrive - students.iitmandi.ac.in/Postgraduation/Semester III/MA605/Data/map/Indian_States.shp")
NWH.plot()
plt.xlabel("Longitude")
plt.ylabel("Latitude")