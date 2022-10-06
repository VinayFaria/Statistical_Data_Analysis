"""
@author: vinay
"""

import pandas as pd
from re import search
from scipy.stats import pearsonr
import matplotlib.pylab as plt

Population_of_Delhi = 20591874
Population_of_Mumbai = 20667656

df1 = pd.read_csv(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\Data\COVID\cowin_vaccine_data_districtwise.csv', sep=',', index_col=False, dtype='unicode')
df2 = pd.read_csv(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\Data\COVID\2021_IN_Region_Mobility_Report.csv')

index_of_mumbai = []
index_of_delhi = []
first_dose_mumbai = {}
first_dose_delhi = {}
second_dose_mumbai = {}
second_dose_delhi = {}
sites_mumbai = {}
sites_delhi = {}
sessions_mumbai = {}
sessions_delhi = {}
Mumbai_Grocery_pharma_mobility = {}
Delhi_Grocery_pharma_mobility = {}
index_states = {}
first_dose_states = {}

for column in df1:    
    # Getting the index of all states
    if column == 'State':
        count = 1
        for row in df1[column]:
            count += 1
            if str(row) == 'nan':
                continue
            elif index_states.get(row) == None:
                index_states[row] = [count]
            else:
                index_states[row].append(count)
    
    # Getting the index of Mumbai
    if column == 'District':
        count = 1
        for row in df1[column]:
            count += 1
            if row == 'Mumbai':
                index_of_mumbai.append(count)
        
    # Getting the index of Delhi
    if column == 'District':
        count = 1
        for row in df1[column]:
            count += 1
            try:
                if search("Delhi", row):
                    index_of_delhi.append(count)
                elif search("Shahdara", row):
                    index_of_delhi.append(count)
            except TypeError:
                continue
    
    dummy = column.replace('.','-')
    date_list = dummy.split('-')
    
    if df1[column][0] == 'First Dose Administered':   # First Dose Administered
        dummy2 = date_list[1] + '_' + date_list[2]
        count = 1
        for row in df1[column]:
            count += 1
            if str(row) == 'nan':
                continue
            else:
                if count in index_of_mumbai:
                    first_dose_mumbai[dummy2] = int(row)/Population_of_Mumbai
                if count in index_of_delhi:
                    if first_dose_delhi.get(dummy2) == None:
                        first_dose_delhi[dummy2] = int(row)
                    else:
                        first_dose_delhi[dummy2] += int(row)
        
        first_dose_delhi[dummy2] = first_dose_delhi[dummy2]/Population_of_Delhi
    
    if df1[column][0] == 'Second Dose Administered':
        dummy2 = date_list[1] + '_' + date_list[2]
        count = 1
        for row in df1[column]:
            count += 1
            if count in index_of_mumbai:
                second_dose_mumbai[dummy2] = int(row)/Population_of_Mumbai
            if count in index_of_delhi:
                if second_dose_delhi.get(dummy2) == None:
                    second_dose_delhi[dummy2] = int(row)
                else:
                    second_dose_delhi[dummy2] += int(row)
        
        second_dose_delhi[dummy2] = second_dose_delhi[dummy2]/Population_of_Delhi

    if df1[column][0] == 'Sites ':
        dummy2 = date_list[1] + '_' + date_list[2]
        count = 1
        for row in df1[column]:
            count += 1
            if count in index_of_mumbai:
                sites_mumbai[dummy2] = int(row)
            if count in index_of_delhi:
                if sites_delhi.get(dummy2) == None:
                    sites_delhi[dummy2] = int(row)
                else:
                    sites_delhi[dummy2] += int(row)
    
    if df1[column][0] == 'Sessions':
        dummy2 = date_list[1] + '_' + date_list[2]
        count = 1
        for row in df1[column]:
            count += 1
            if count in index_of_mumbai:
                sessions_mumbai[dummy2] = int(row)
            if count in index_of_delhi:
                if sessions_delhi.get(dummy2) == None:
                    sessions_delhi[dummy2] = int(row)
                else:
                    sessions_delhi[dummy2] += int(row)

first_dose_Mumbai_list = first_dose_mumbai.items() # return a list of tuples
first_dose_Delhi_list = first_dose_delhi.items() # return a list of tuples
second_dose_Mumbai_list = second_dose_mumbai.items() # return a list of tuples
second_dose_Delhi_list = second_dose_delhi.items() # return a list of tuples

x1, y1 = zip(*first_dose_Mumbai_list) # unpack a list of pairs into two tuples
x2, y2 = zip(*first_dose_Delhi_list) # unpack a list of pairs into two tuples
x3, y3 = zip(*second_dose_Mumbai_list) # unpack a list of pairs into two tuples
x4, y4 = zip(*second_dose_Delhi_list) # unpack a list of pairs into two tuples

plt.figure() # Used to create a figure
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.legend(['First dose Mumbai','First dose Delhi','Second dose Mumbai','Second dose Delhi'])
plt.title('Vaccination coverage')
plt.xticks(rotation = 45) # Rotates X-Axis Ticks by 45-degrees
plt.xlabel('Time (Months)')
plt.ylabel('Number of vaccination')
plt.tight_layout() # If not used x-axis label gets cropped
plt.grid()
plt.show()

site_mumbai_value = [sites_mumbai[d] for d in sites_mumbai]
corr, _ = pearsonr(y1, site_mumbai_value)
print('Pearsons correlation between first dose coverage and sites in Mumbai: %.3f' % corr)

site_delhi_value = [sites_delhi[d] for d in sites_delhi]
corr, _ = pearsonr(y2, site_delhi_value)
print('Pearsons correlation between first dose coverage and sites in Delhi: %.3f' % corr)

sessions_mumbai_value = [sessions_mumbai[d] for d in sessions_mumbai]
corr, _ = pearsonr(y1, sessions_mumbai_value)
print('Pearsons correlation between first dose coverage and sessions in Mumbai: %.3f' % corr)

sessions_delhi_value = [sessions_delhi[d] for d in sessions_delhi]
corr, _ = pearsonr(y2, sessions_delhi_value)
print('Pearsons correlation between first dose coverage and sessions in Delhi: %.3f' % corr)

for ind in df2.index:
    if df2['sub_region_2'][ind] == 'Mumbai' or df2['sub_region_2'][ind] == 'Mumbai Suburban':
        dummy1 = df2['date'][ind]
        date_list = dummy1.split('-')
        dummy2 = date_list[1] + '_' + date_list[0]
        
        if Mumbai_Grocery_pharma_mobility.get(dummy2) == None:
            Mumbai_Grocery_pharma_mobility[dummy2] = df2['retail_and_recreation_percent_change_from_baseline'][ind]
        else:
            Mumbai_Grocery_pharma_mobility[dummy2] += df2['retail_and_recreation_percent_change_from_baseline'][ind]
        
    if df2['sub_region_1'][ind] == 'Delhi':
        dummy1 = df2['date'][ind]
        date_list = dummy1.split('-')
        dummy2 = date_list[1] + '_' + date_list[0]
        
        if Delhi_Grocery_pharma_mobility.get(dummy2) == None:
            Delhi_Grocery_pharma_mobility[dummy2] = df2['transit_stations_percent_change_from_baseline'][ind]
        else:
            Delhi_Grocery_pharma_mobility[dummy2] += df2['transit_stations_percent_change_from_baseline'][ind]

for i in range(2):
    Mumbai_Grocery_pharma_mobility.popitem()
    Delhi_Grocery_pharma_mobility.popitem()

Grocery_pharma_mumbai_value = [Mumbai_Grocery_pharma_mobility[d] for d in Mumbai_Grocery_pharma_mobility]
Grocery_pharma_delhi_value = [Delhi_Grocery_pharma_mobility[d] for d in Delhi_Grocery_pharma_mobility]
   
corr, _ = pearsonr(y1, Grocery_pharma_mumbai_value)
print('Pearsons correlation between first dose coverage and Grocery pharma in Mumbai: %.3f' % corr)

corr, _ = pearsonr(y2, Grocery_pharma_delhi_value)
print('Pearsons correlation between first dose coverage and Grocery pharma in Delhi: %.3f' % corr)

count = 0
for row in df1["31-10-2021.3"]:
    count += 1
    if str(row) == 'nan':
        continue
    else:
        for key, value in index_states.items():
            if count in value:
                if first_dose_states.get(key) == None:
                    first_dose_states[key] = int(row)
                else:
                    first_dose_states[key] += int(row)
print("Maximum number of doses are in state", max(first_dose_states, key= lambda x: first_dose_states[x]))