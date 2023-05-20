import altair as alt
import numpy as np
import pandas as pd
from vega_datasets import data
flight  = pd.read_csv('UKflights.csv')
airport  = pd.read_csv('EU_airport.csv')
# flight = flight.loc[flight['YEAR'] == 2020]
# icao =flight['APT_ICAO'].unique()
# print(icao)
# data1 = pd.DataFrame(columns=['ICAO','Year','Departures','Arrivals','Longitude','Latitude','Name'])
# data1['ICAO'] = icao
# data1['Year'] = 2020
# for index, row in data1.iterrows():
#   departure = 0
#   alpha = row['ICAO']
#   for  index2, row2 in flight.iterrows():
#     if  alpha == row2['APT_ICAO']:
#       departure = departure + row2['FLT_ARR_1']
#   print(departure)
#   # data.iloc[index]['Arrivals'] = departure
#   data1.at[index,'Arrivals'] = departure
# data1.to_csv('2020.csv')

####################################################################################################################################
data1   = pd.read_csv('2020.csv')
for index, row in data1.iterrows():
  alpha = row['ICAO']

  for  index2, row2 in airport.iterrows():
     if  alpha == row2['ident']:
       print(alpha)
       data1.at[index,'Longitude'] = row2['longitude_deg']
       data1.at[index,'Latitude'] = row2['latitude_deg']
       data1.at[index,'Name'] = row2['name']

data1.to_csv('2020_2.csv')

# df1 =pd.read_csv('2017_2.csv')
# df2 = pd.read_csv('2016_2.csv')
# df3 = pd.concat([df1, df2], axis=0)
# df3.to_csv('final.csv')