"""
@author: vinay
Aim: Finding rainfall and temperature correlation
"""

import pandas as pd
import numpy as np
import seaborn as sns
import geopandas as  gpd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
from shapely.geometry import Point
from geopandas import GeoDataFrame

rain_df = pd.read_csv(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\Data\climate\NWH-CRU_pre_1901-2020_month_50km.csv', header=None)
temperature_df = pd.read_csv(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\Data\climate\NWH-CRU_tmp_1901-2020_month_50km.csv', header=None)

count = 0
correlation_rain_temp_df = pd.DataFrame(columns = ['years'])
for dummy in range(1901, 2021):
    correlation_rain_temp_df = correlation_rain_temp_df.append({'years': dummy}, ignore_index=True)

years = np.array([])
average_rain = np.array([])
average_temp = np.array([])
per_year_rain = np.array([])
per_year_temperature = np.array([])
correlation_rain_temp = np.array([])
for ind in rain_df.index:
    year = 1900
    correlation_rain_temp_df[str(rain_df[0][ind])+str(rain_df[1][ind])] = np.nan
    for i in range(2,len(temperature_df.columns)):
        count += 1
        per_year_rain = np.append(per_year_rain, rain_df.iloc[ind][i])
        per_year_temperature = np.append(per_year_temperature, temperature_df.iloc[ind][i])
        if count == 12:
            year += 1
            years = np.append(years, year)
            corr, _ = pearsonr(per_year_rain, per_year_temperature)
            correlation_rain_temp_df.loc[correlation_rain_temp_df.years == year, str(rain_df[0][ind])+str(rain_df[1][ind])] = corr
            per_year_rain = np.array([])
            per_year_temperature = np.array([])
            count = 0
    correlation_rain_temp = np.array([])
    years = np.array([])

years = correlation_rain_temp_df.years.unique().tolist()
correlation_rain_temp_df.set_index('years', inplace=True)
#heatmap_data = correlation_rain_temp_df.loc[years]
plt.figure(1)
sns.heatmap(correlation_rain_temp_df, vmin = -1, vmax = 1, cbar_kws={'label': 'Pearson correlation coefficient'})
# plt.figure(2)
# sns.pairplot(correlation_rain_temp_df)
#plt.xlabel("locations")
#plt.ylabel("Years")
#plt.title("Correlation of rainfall and temperature for different location and year")
#plt.tight_layout()
#geometry = [Point(xy) for xy in zip(df['x'], df['y'])]
#gdf = GeoDataFrame(df, geometry = geometry)

#nhr = gpd.read_file(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\Data\map\4_17_2018_899072.shp')
#gdf.plot(ax=nhr.plot(figsize=(5, 5)), marker='o', color='red', markersize=6);

#plt.scatter(df['x'], df['y'])

#nhr_df = pd.read_csv(r'D:\Postgraduation\OneDrive - students.iitmandi.ac.in\Postgraduation\Semester III\MA605\Data\climate\NWH_temp_data_25_1901_2017_cru_data.csv')
#nhr_df = nhr_df.iloc[: , :-3] # remove last 3 column

#plt.figure()
#boxplot = nhr_df.boxplot(column=['X74.7532.5', 'X79.2529', 'X79.529.25'])

# To find the correlation among the columns using pearson method
#dummy = nhr_df.corr(method ='pearson')

#print(nhr_df.corr(method ='pearson'))
#fig, ax = plt.subplots(figsize=(10, 6))
#sns.heatmap(nhr_df.corr(), ax=ax, annot=True)
# plotting correlation heatmap
#dataplot = sns.heatmap(nhr_df.corr(method ='pearson'), cmap="YlGnBu", annot=True)
  
# # displaying heatmap
# plt.show()