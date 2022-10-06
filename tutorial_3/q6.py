"""
@author: Vinay
Question: Plot the shape file of north-western Himalaya region.
Dataset: 4_17_2018_899072.shp
"""

import geopandas
import matplotlib.pyplot as plt

#df = pd.read_csv(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\Data\climate\latlongNWH.csv')
#plt.scatter(df.x, df.y, color='red')

NWH = geopandas.read_file("D:/Postgraduation/OneDrive - students.iitmandi.ac.in/Postgraduation/Semester III/MA605/Data/map/4_17_2018_899072.shp")
NWH.plot()
plt.xlabel("Longitude")
plt.ylabel("Latitude")