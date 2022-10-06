"""
@author: vinay
"""

import pandas as pd
import numpy as np
import seaborn as sns
from scipy.stats import skew
from scipy.stats import norm
import matplotlib.pyplot as plt

rain_df = pd.read_csv(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\Data\climate\NWH-CRU_pre_1901-2020_month_50km.csv', header=None)
temperature_df = pd.read_csv(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\Data\climate\NWH-CRU_tmp_1901-2020_month_50km.csv', header=None)

average_rain = np.array([])
average_temp = np.array([])
per_year_rain = np.array([])
per_year_temperature = np.array([])
count = 0

for i in range(2,len(temperature_df.columns)):
    count += 1
    per_year_rain = np.append(per_year_rain, rain_df.iloc[2][i])
    per_year_temperature = np.append(per_year_temperature, temperature_df.iloc[2][i])
    if count == 12:
        average_rain = np.append(average_rain, sum(per_year_rain)/12)
        average_temp = np.append(average_temp, sum(per_year_temperature)/12)
        per_year_rain = np.array([])
        per_year_temperature = np.array([])
        count = 0
        
hmean = np.mean(average_rain)
hmedian = np.median(average_rain)
hstd = np.std(average_rain)

f, (ax_box, ax_hist) = plt.subplots(nrows=2, sharex=True, gridspec_kw = {"height_ratios": (0.2, 1)})
sns.boxplot(data=average_rain, orient="h", ax=ax_box)
ax_box.axvline(hmean, color='r', linestyle='--')
ax_box.axvline(hmedian, color='g', linestyle='-')
sns.histplot(average_rain, ax=ax_hist, stat="density", bins=30)
ax_hist.axvline(hmean, color='r', linestyle='--')
ax_hist.axvline(hmedian, color='g', linestyle='-')
plt.legend({'Mean':hmean,'Median':hmedian})
ax_box.set(xlabel='')

# Plot the PDF.
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, hmean, hstd)
plt.plot(x, p, 'k', linewidth=2)
plt.show()

print('Skewness of rain: {}'.format(skew(average_rain)))
print('Skewness of temperature: {}'.format(skew(average_temp)))