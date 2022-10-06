"""
@author: vinay
"""

import pandas as pd
import matplotlib.pylab as plt

Population_of_Delhi = 20591874
Population_of_Mumbai = 20667656
Population_of_Kolkata = 14900000

Delhi_dict = {}
Kolkata_dict = {}
Mumbai_dict = {}

df = pd.read_csv(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\Data\COVID\districts.csv')

for ind in df.index:
    dummy1 = df['Date'][ind]
    date_list = dummy1.split('-')
    dummy2 = date_list[1] + '_' + date_list[0]
    
    if df['District'][ind] == 'Mumbai':
        if Mumbai_dict.get(dummy2) == None:
            Mumbai_dict[dummy2] = df['Confirmed'][ind] - df['Recovered'][ind] - df['Deceased'][ind]
        else:
            Mumbai_dict[dummy2] += df['Confirmed'][ind] - df['Recovered'][ind] - df['Deceased'][ind]
    elif df['District'][ind] == 'Delhi':
        if Delhi_dict.get(dummy2) == None:
            Delhi_dict[dummy2] = df['Confirmed'][ind] - df['Recovered'][ind] - df['Deceased'][ind]
        else:
            Delhi_dict[dummy2] += df['Confirmed'][ind] - df['Recovered'][ind] - df['Deceased'][ind]
    elif df['District'][ind] == 'Kolkata':
        if Kolkata_dict.get(dummy2) == None:
            Kolkata_dict[dummy2] = df['Confirmed'][ind] - df['Recovered'][ind] - df['Deceased'][ind]
        else:
            Kolkata_dict[dummy2] += df['Confirmed'][ind] - df['Recovered'][ind] - df['Deceased'][ind]

mean_mumbai_case = 0
mean_delhi_case = 0
mean_kolkata_case = 0
count = 0

for key in Mumbai_dict:
    mean_mumbai_case += Mumbai_dict[key]
    mean_delhi_case += Delhi_dict[key]
    mean_kolkata_case += Kolkata_dict[key]
    count += 1

mean_mumbai_case = mean_mumbai_case/count
mean_delhi_case = mean_delhi_case/count
mean_kolkata_case = mean_kolkata_case/count

sum_of_square_mumbai = 0
sum_of_square_delhi = 0
sum_of_square_kolkata = 0

for key in Mumbai_dict:
    sum_of_square_mumbai += (Mumbai_dict[key]-mean_mumbai_case)**2
    sum_of_square_delhi += (Delhi_dict[key]-mean_delhi_case)**2
    sum_of_square_kolkata += (Kolkata_dict[key]-mean_kolkata_case)**2

variance_mumbai = sum_of_square_mumbai/count
variance_delhi = sum_of_square_delhi/count
variance_kolkata = sum_of_square_kolkata/count

print("variance of the infected in mumbai is ", variance_mumbai)
print("variance of the infected in delhi is ", variance_delhi)
print("variance of the infected in kolkata is ", variance_kolkata)

for key in Mumbai_dict:
    Mumbai_dict[key] = Mumbai_dict[key]/Population_of_Mumbai
    Delhi_dict[key] = Delhi_dict[key]/Population_of_Delhi
    Kolkata_dict[key] = Kolkata_dict[key]/Population_of_Kolkata

Mumbai_list = Mumbai_dict.items() # return a list of tuples
Delhi_list = Delhi_dict.items() # return a list of tuples
Kolkata_list = Kolkata_dict.items() # return a list of tuples

x1, y1 = zip(*Mumbai_list) # unpack a list of pairs into two tuples
x2, y2 = zip(*Delhi_list) # unpack a list of pairs into two tuples
x3, y3 = zip(*Kolkata_list) # unpack a list of pairs into two tuples

plt.figure() # Used to create a figure
plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.legend(['Infected fraction for Mumbai','Infected fraction for Delhi','Infected fraction for Kolkata'])
plt.title('Time graph of the infected fraction of population')
plt.xticks(rotation = 45) # Rotates X-Axis Ticks by 45-degrees
plt.xlabel('Time (Months)')
plt.ylabel('Infected fraction')
plt.tight_layout() # If not used x-axis label gets cropped
plt.grid()
plt.show()