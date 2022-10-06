"""
@author: Vinay
Question: Plot the mean temperature over 528 grids of North-Western Himalayas.
Dataset: NWH_temp_data_25_1901_2017_cru_data, latlongNWH
"""
import geopandas
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
columns = ['x','y']
df1 = pd.read_csv(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\Data\climate\NWH_temp_data_25_1901_2017_cru_data.csv')
df2 = pd.DataFrame(columns=columns)

NWH = geopandas.read_file("D:/Postgraduation/OneDrive - students.iitmandi.ac.in/Postgraduation/Semester III/MA605/Data/map/4_17_2018_899072.shp")
#NWH.plot()

count = 0
per_year_temperature = 0
#years = np.array([])
average_temp = np.array([])
count_1 = 0
for column in df1:
    #year = 1900
    dummy = column[1:]
    if len(dummy) == 4:
        df2.loc[count_1] = [float(dummy[:2])] + [float(dummy[2:])]
    elif len(dummy) == 6 and dummy[2] == '.':
        df2.loc[count_1] = [float(dummy[:4])] + [float(dummy[4:])]
    elif len(dummy) == 6 and dummy[4] == '.':
        df2.loc[count_1] = [float(dummy[:2])] + [float(dummy[2:])]
    elif len(dummy) == 7 and dummy[2] == '.':
        df2.loc[count_1] = [float(dummy[:5])] + [float(dummy[5:])]
    elif len(dummy) == 7 and dummy[4] == '.':
        df2.loc[count_1] = [float(dummy[:2])] + [float(dummy[2:])]
    elif len(dummy) == 8:
        df2.loc[count_1] = [float(dummy[:4])] + [float(dummy[4:])]
    elif len(dummy) == 9 and dummy[2] == '.' and dummy[7] == '.':
        df2.loc[count_1] = [float(dummy[:5])] + [float(dummy[5:])]
    elif len(dummy) == 9 and dummy[2] == '.' and dummy[6] == '.':
        df2.loc[count_1] = [float(dummy[:4])] + [float(dummy[4:])]
    elif len(dummy) == 10:
        df2.loc[count_1] = [float(dummy[:5])] + [float(dummy[5:])]
    count_1 += 1
    for row in df1[column]:
        count += 1
        per_year_temperature += row
        if count == 1404:
            #year += 1
            #years = np.append(years, year)
            average_temp = np.append(average_temp, per_year_temperature/1404)
            per_year_temperature = 0
            count = 0

# latest_average_temp = np.array([])
# for dummy in average_temp:
#     count +=1
#     if count == 117:
#         latest_average_temp = np.append(latest_average_temp, dummy)
#         count = 0
# latest_average_temp = np.append(latest_average_temp, 'nan')
# df2['mean_temp'] = latest_average_temp

# Deleting last 3 nan values
for i in range(3):
    average_temp = np.delete(average_temp, -1)

minVal =  np.min(average_temp)
maxVal =  np.max(average_temp)

#average_temp = np.append(average_temp)
df2['mean_temp'] = average_temp

# Dropping last 4 rows because it contain nan: Not A Number 
df2.drop(df2.tail(4).index,inplace = True)

colors = df2['mean_temp'].astype(float)
int_array  = colors.astype(int)
image = plt.scatter(df2.x, df2.y, c = int_array, vmin=minVal,vmax = maxVal)
plt.xticks(rotation = 45) # Rotates X-Axis Ticks by 45-degrees

v = np.linspace(minVal, maxVal, 15, endpoint=True)

plt.show()
plt.xlabel("Longitude")
plt.ylabel("Latitude")

clb = plt.colorbar(image, ticks = v)
clb.ax.set_title('Mean temperature(°C)')
# # Get the default ticks and tick labels
# ticklabels = cbar.ax.get_ymajorticklabels()
# ticks = list(cbar.get_ticks())

# # Append the ticks (and their labels) for minimum and the maximum value
# cbar.set_ticks([minVal, maxVal])
# cbar.set_ticklabels([minVal, maxVal])

# plt.show()