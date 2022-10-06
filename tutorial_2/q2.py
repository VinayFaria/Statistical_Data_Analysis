"""
@author: vinay
"""

import pandas as pd
import numpy as np
import matplotlib.pylab as plt

df = pd.read_csv(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\Data\COVID\2021_IN_Region_Mobility_Report.csv')

Mumbai_retail_dict = {}
Delhi_retail_dict = {}
Mumbai_transit_dict = {}
Delhi_transit_dict = {}
Mumbai_retail_arr = np.array([])
Delhi_retail_arr = np.array([])
Mumbai_transit_arr = np.array([])
Delhi_transit_arr = np.array([])
mumbai_25th_retail_quartile_arr = np.array([])
mumbai_75th_retail_quartile_arr = np.array([])
mumbai_25th_transit_quartile_arr = np.array([])
mumbai_75th_transit_quartile_arr = np.array([])
delhi_25th_retail_quartile_arr = np.array([])
delhi_75th_retail_quartile_arr = np.array([])
delhi_25th_transit_quartile_arr = np.array([])
delhi_75th_transit_quartile_arr = np.array([])

for ind in df.index:
    if df['sub_region_2'][ind] == 'Mumbai' or df['sub_region_2'][ind] == 'Mumbai Suburban':
        dummy1 = df['date'][ind]
        date_list = dummy1.split('-')
        dummy2 = date_list[1] + '_' + date_list[0]
        
        Mumbai_retail_arr = np.append(Mumbai_retail_arr, df['retail_and_recreation_percent_change_from_baseline'][ind]) # This line is added for calculating IQR
        Mumbai_transit_arr = np.append(Mumbai_transit_arr, df['transit_stations_percent_change_from_baseline'][ind])    # This line is added for calculating IQR
        
        if Mumbai_retail_dict.get(dummy2) == None:
            Mumbai_retail_dict[dummy2] = df['retail_and_recreation_percent_change_from_baseline'][ind]
        else:
            Mumbai_retail_dict[dummy2] += df['retail_and_recreation_percent_change_from_baseline'][ind]
        
        if Mumbai_transit_dict.get(dummy2) == None:
            Mumbai_transit_dict[dummy2] = df['transit_stations_percent_change_from_baseline'][ind]
        else:
            Mumbai_transit_dict[dummy2] += df['transit_stations_percent_change_from_baseline'][ind]        
    
    if df['sub_region_1'][ind] == 'Delhi':
        dummy1 = df['date'][ind]
        date_list = dummy1.split('-')
        dummy2 = date_list[1] + '_' + date_list[0]
        
        Delhi_retail_arr = np.append(Delhi_retail_arr, df['retail_and_recreation_percent_change_from_baseline'][ind])
        Delhi_transit_arr = np.append(Delhi_transit_arr, df['transit_stations_percent_change_from_baseline'][ind])
        
        if Delhi_retail_dict.get(dummy2) == None:
            Delhi_retail_dict[dummy2] = df['retail_and_recreation_percent_change_from_baseline'][ind]
        else:
            Delhi_retail_dict[dummy2] += df['retail_and_recreation_percent_change_from_baseline'][ind]
        
        if Delhi_transit_dict.get(dummy2) == None:
            Delhi_transit_dict[dummy2] = df['transit_stations_percent_change_from_baseline'][ind]
        else:
            Delhi_transit_dict[dummy2] += df['transit_stations_percent_change_from_baseline'][ind]
    
Mumbai_list = Mumbai_retail_dict.items() # return a list of tuples
Delhi_list = Delhi_retail_dict.items() # return a list of tuples

x1, y1 = zip(*Mumbai_list) # unpack a list of pairs into two tuples
x2, y2 = zip(*Delhi_list) # unpack a list of pairs into two tuples
plt.figure(1) # Used to create a figure
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.legend(['Retail mobility of Mumbai','Retail mobility of Delhi'])
plt.title('Retail mobility')
plt.xticks(rotation = 45) # Rotates X-Axis Ticks by 45-degrees
plt.xlabel('Time (Months)')
plt.ylabel('Mobility')
plt.tight_layout() # If not used x-axis label gets cropped
plt.grid()

Mumbai_list = Mumbai_transit_dict.items() # return a list of tuples
Delhi_list = Delhi_transit_dict.items() # return a list of tuples
x1, y1 = zip(*Mumbai_list) # unpack a list of pairs into two tuples
x2, y2 = zip(*Delhi_list) # unpack a list of pairs into two tuples
plt.figure(2) # Used to create a figure
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.legend(['Transit mobility of Mumbai','Transit mobility of Delhi'])
plt.title('Transit mobility')
plt.xticks(rotation = 45) # Rotates X-Axis Ticks by 45-degrees
plt.xlabel('Time (Months)')
plt.ylabel('Mobility')
plt.tight_layout() # If not used x-axis label gets cropped
plt.grid()

plt.show()

Mumbai_retail_arr = np.sort(Mumbai_retail_arr)
Mumbai_transit_arr = np.sort(Mumbai_transit_arr)
Delhi_retail_arr = np.sort(Delhi_retail_arr)
Delhi_transit_arr = np.sort(Delhi_transit_arr)

median_mumbai_retail = np.median(Mumbai_retail_arr)
median_mumbai_transit = np.median(Mumbai_transit_arr)
median_delhi_retail = np.median(Delhi_retail_arr)
median_delhi_transit = np.median(Delhi_transit_arr)

for element in Mumbai_retail_arr:
    if element > median_mumbai_retail:
        mumbai_75th_retail_quartile_arr = np.append(mumbai_75th_retail_quartile_arr, element)
    else:
        mumbai_25th_retail_quartile_arr = np.append(mumbai_25th_retail_quartile_arr, element)
for element in Mumbai_transit_arr:
    if element > median_mumbai_transit:
        mumbai_75th_transit_quartile_arr = np.append(mumbai_75th_transit_quartile_arr, element)
    else:
        mumbai_25th_transit_quartile_arr = np.append(mumbai_25th_transit_quartile_arr, element)
for element in Delhi_retail_arr:
    if element > median_delhi_retail:
        delhi_75th_retail_quartile_arr = np.append(delhi_75th_retail_quartile_arr, element)
    else:
        delhi_25th_retail_quartile_arr = np.append(delhi_25th_retail_quartile_arr, element)
for element in Delhi_transit_arr:
    if element > median_delhi_retail:
        delhi_75th_transit_quartile_arr = np.append(delhi_75th_transit_quartile_arr, element)
    else:
        delhi_25th_transit_quartile_arr = np.append(delhi_25th_transit_quartile_arr, element)

IQR_mumbai_retail = np.median(mumbai_75th_retail_quartile_arr) - np.median(mumbai_25th_retail_quartile_arr)
IQR_mumbai_transit = np.median(mumbai_75th_transit_quartile_arr) - np.median(mumbai_25th_transit_quartile_arr)
IQR_delhi_retail = np.median(delhi_75th_retail_quartile_arr) - np.median(delhi_25th_retail_quartile_arr)
IQR_delhi_transit = np.median(delhi_75th_transit_quartile_arr) - np.median(delhi_25th_transit_quartile_arr)

mean_mumbai_retail = np.mean(Mumbai_retail_arr)
mean_mumbai_transit = np.mean(Mumbai_transit_arr)
mean_delhi_retail = np.mean(Delhi_retail_arr)
mean_delhi_transit = np.mean(Delhi_transit_arr)