"""
@author: vinay
Aim: Viewing the skewness in graph
The rule isn't that all the bars should sum to one. The rule is that all the areas of all the bars should sum to one.
"""

import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats
from scipy.stats import skew
from scipy.stats import norm
import matplotlib.pyplot as plt

rain_df = pd.read_csv(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\Data\climate\NWH-CRU_pre_1901-2020_month_50km.csv', header=None)
temperature_df = pd.read_csv(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\Data\climate\NWH-CRU_tmp_1901-2020_month_50km.csv', header=None)

skewness_dict = pd.DataFrame(columns = ["latitude", "longitude", "Rain_skewness", "Temperature_skewness"])
average_rain = np.array([])
average_temp = np.array([])
per_year_rain = np.array([])
per_year_temperature = np.array([])
count = 0

for ind in rain_df.index:
    for i in range(2,len(temperature_df.columns)):
        count += 1
        per_year_rain = np.append(per_year_rain, rain_df.iloc[ind][i])
        per_year_temperature = np.append(per_year_temperature, temperature_df.iloc[ind][i])
        if count == 12:
            average_rain = np.append(average_rain, sum(per_year_rain)/12)
            average_temp = np.append(average_temp, sum(per_year_temperature)/12)
            per_year_rain = np.array([])
            per_year_temperature = np.array([])
            count = 0
    
    # Removing outliers
    average_rain_df = pd.DataFrame(data = average_rain, columns=['0'])
    average_temp_df = pd.DataFrame(data = average_temp, columns=['0'])
    rain_Q1 = average_rain_df['0'].quantile(0.25)
    rain_Q3 = average_rain_df['0'].quantile(0.75)
    temp_Q1 = average_temp_df['0'].quantile(0.25)
    temp_Q3 = average_temp_df['0'].quantile(0.75)
    rain_IQR = rain_Q3 - rain_Q1    #IQR is interquartile range.
    temp_IQR = temp_Q3 - temp_Q1    #IQR is interquartile range. 
    rain_filter = (average_rain_df['0'] >= rain_Q1 - 1.5 * rain_IQR) & (average_rain_df['0'] <= rain_Q3 + 1.5 *rain_IQR)
    temp_filter = (average_temp_df['0'] >= temp_Q1 - 1.5 * temp_IQR) & (average_temp_df['0'] <= temp_Q3 + 1.5 *temp_IQR)
    average_rain_new = average_rain_df.loc[rain_filter]
    average_temp_new = average_temp_df.loc[temp_filter]
    average_rain_new = average_rain_new.to_numpy()
    average_temp_new = average_temp_new.to_numpy()
    
    if ind == 217:  # Specify the grid point for viewing boxplot, gaussian
        print(skew(average_rain), skew(average_rain_new), skew(average_temp), skew(average_temp_new))
        rmean = np.mean(average_rain_new)
        rmedian = np.median(average_rain_new)
        rstd = np.std(average_rain_new)
        f1, (ax_box1, ax_hist1) = plt.subplots(nrows=2, sharex=True, gridspec_kw = {"height_ratios": (0.2, 1)})
        sns.boxplot(data=average_rain_new, orient="h", ax=ax_box1)
        ax_box1.axvline(rmean, color='r', linestyle='--')
        ax_box1.axvline(rmedian, color='g', linestyle='-')
        sns.histplot(average_rain_new, ax=ax_hist1, stat="density", bins=30)
        ax_hist1.axvline(rmean, color='r', linestyle='--')
        ax_hist1.axvline(rmedian, color='g', linestyle='-')
        plt.legend({'Mean':rmean,'Median':rmedian})
        plt.xlabel('Rainfall')
        plt.ylabel('')
        f1.suptitle('Plot for location: Longitude {}, Latitude {}'.format(rain_df.iloc[ind][0],rain_df.iloc[ind][1]))
        #ax_box1.set(xlabel='')

        # Plot the PDF.
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, rmean, rstd)
        plt.plot(x, p, 'k', linewidth=2)
        plt.title('Rain skewness: {}'.format(skew(average_rain_new)[0]))
        
        tmean = np.mean(average_temp_new)
        tmedian = np.median(average_temp_new)
        tstd = np.std(average_temp_new)
        f2, (ax_box2, ax_hist2) = plt.subplots(nrows=2, sharex=True, gridspec_kw = {"height_ratios": (0.2, 1)})
        sns.boxplot(data=average_temp_new, orient="h", ax=ax_box2)
        ax_box2.axvline(tmean, color='r', linestyle='--')
        ax_box2.axvline(tmedian, color='g', linestyle='-')
        sns.histplot(average_temp_new, ax=ax_hist2, stat="density", bins=30)
        ax_hist2.axvline(tmean, color='r', linestyle='--')
        ax_hist2.axvline(tmedian, color='g', linestyle='-')
        plt.legend({'Mean':tmean,'Median':tmedian})
        plt.xlabel('Temperature (°C)')
        plt.ylabel('')
        f2.suptitle('Plot for location: Longitude {}, Latitude {}'.format(rain_df.iloc[ind][0],rain_df.iloc[ind][1]))
        #ax_box2.set(xlabel='')

        # Plot the PDF.
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, tmean, tstd)
        plt.plot(x, p, 'k', linewidth=2)
        plt.show()
        plt.title('Temperature skewness: {}'.format(skew(average_temp_new)[0]))
        
        rmean = np.mean(average_rain)
        rmedian = np.median(average_rain)
        rstd = np.std(average_rain)
        f3, (ax_box3, ax_hist3) = plt.subplots(nrows=2, sharex=True, gridspec_kw = {"height_ratios": (0.2, 1)})
        sns.boxplot(data=average_rain, orient="h", ax=ax_box3)
        ax_box3.axvline(rmean, color='r', linestyle='--')
        ax_box3.axvline(rmedian, color='g', linestyle='-')
        sns.histplot(average_rain, ax=ax_hist3, stat="density", bins=30)
        ax_hist3.axvline(rmean, color='r', linestyle='--')
        ax_hist3.axvline(rmedian, color='g', linestyle='-')
        plt.legend({'Mean':rmean,'Median':rmedian})
        plt.xlabel('Rainfall')
        plt.ylabel('')
        f3.suptitle('Plot for location: Longitude {}, Latitude {}'.format(rain_df.iloc[ind][0],rain_df.iloc[ind][1]))
        #ax_box1.set(xlabel='')

        # Plot the PDF.
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, rmean, rstd)
        plt.plot(x, p, 'k', linewidth=2)
        plt.title('Rain skewness: {}'.format(skew(average_rain)))
        
        tmean = np.mean(average_temp)
        tmedian = np.median(average_temp)
        tstd = np.std(average_temp)
        f4, (ax_box4, ax_hist4) = plt.subplots(nrows=2, sharex=True, gridspec_kw = {"height_ratios": (0.2, 1)})
        sns.boxplot(data=average_temp, orient="h", ax=ax_box4)
        ax_box4.axvline(tmean, color='r', linestyle='--')
        ax_box4.axvline(tmedian, color='g', linestyle='-')
        sns.histplot(average_temp, ax=ax_hist4, stat="density", bins=30)
        ax_hist4.axvline(tmean, color='r', linestyle='--')
        ax_hist4.axvline(tmedian, color='g', linestyle='-')
        plt.legend({'Mean':tmean,'Median':tmedian})
        plt.xlabel('Temperature (°C)')
        plt.ylabel('')
        f4.suptitle('Plot for location: Longitude {}, Latitude {}'.format(rain_df.iloc[ind][0],rain_df.iloc[ind][1]))
        #ax_box2.set(xlabel='')

        # Plot the PDF.
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, tmean, tstd)
        plt.plot(x, p, 'k', linewidth=2)
        plt.show()
        plt.title('Temperature skewness: {}'.format(skew(average_temp)))
    skewness_dict = skewness_dict.append({'longitude':rain_df.iloc[ind][0], 'latitude':rain_df.iloc[ind][1], 'Rain_skewness': skew(average_rain), 'Temperature_skewness': skew(average_temp)}, ignore_index=True)
    average_rain = np.array([])
    average_temp = np.array([])

# plt.scatter(skewness_dict['Rain_skewness'], skewness_dict['Temperature_skewness'])
# plt.xlabel("Rain_skewness for location")
# plt.ylabel("Temperature_skewness for location")