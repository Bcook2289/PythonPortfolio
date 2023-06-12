import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


data = pd.read_csv("global_power_plant_database.csv", low_memory=False)
pd.set_option('display.max_columns', None)

print(data.head())

gen_growth = data[['country', 'capacity_mw', 'primary_fuel', 'generation_gwh_2013', 'generation_gwh_2014',
                   'generation_gwh_2015', 'generation_gwh_2016', 'generation_gwh_2017', 'generation_gwh_2018',
                   'generation_gwh_2019']].copy()

gen_growth.dropna(subset=['generation_gwh_2013', 'generation_gwh_2014', 'generation_gwh_2015', 'generation_gwh_2016',
                          'generation_gwh_2017', 'generation_gwh_2018', 'generation_gwh_2019'], inplace=True)

fuel_group = gen_growth.groupby('primary_fuel')

total_generation_by_fuel = fuel_group[['generation_gwh_2013', 'generation_gwh_2014', 'generation_gwh_2015',
                                       'generation_gwh_2016', 'generation_gwh_2017', 'generation_gwh_2018',
                                       'generation_gwh_2019']].sum()

sorted_generation = total_generation_by_fuel.sum(axis=1).sort_values(ascending=False)

plt.bar(sorted_generation.index.astype(str), sorted_generation)
plt.xlabel('Primary Fuel Type')
plt.ylabel('Total Energy Generation (GWh)')
plt.title('Energy Generation in the US by Fuel Type')
plt.xticks(rotation=90)
plt.show()

gen_growth.rename(columns={'generation_gwh_2013': '2013',
                           'generation_gwh_2014': '2014',
                           'generation_gwh_2015': '2015',
                           'generation_gwh_2016': '2016',
                           'generation_gwh_2017': '2017',
                           'generation_gwh_2018': '2018',
                           'generation_gwh_2019': '2019'}, inplace=True)

selected_fuels = ['Coal', 'Gas', 'Hydro', 'Nuclear', 'Solar', 'Wind']
gen_growth_filtered = gen_growth[gen_growth['primary_fuel'].isin(selected_fuels)]

generation_by_fuel = gen_growth_filtered.groupby('primary_fuel')[['2013', '2014', '2015', '2016', '2017', '2018',
                                                                  '2019']].sum()


generation_by_fuel = generation_by_fuel.transpose()

plt.plot(generation_by_fuel.index, generation_by_fuel.values)
plt.xlabel('Year')
plt.ylabel('Total in Energy Generation(GWh)')
plt.title('Change in Energy Generation in the US (2013-2019) by Fuel Type')
plt.legend(generation_by_fuel.columns)
plt.xticks(rotation=90)
plt.show()

nuclear_data = gen_growth[gen_growth['primary_fuel'] == 'Nuclear']
gas_data = gen_growth[gen_growth['primary_fuel'] == 'Gas']

plt.scatter(nuclear_data['capacity_mw'], nuclear_data['2019'], label='Nuclear')
plt.scatter(gas_data['capacity_mw'], gas_data['2019'], label='Gas')

nuclear_capacity = nuclear_data['capacity_mw'].values.reshape(-1, 1)
nuclear_generation = nuclear_data['2019'].values.reshape(-1, 1)
nuclear_slope, nuclear_intercept = np.polyfit(nuclear_capacity.flatten(), nuclear_generation.flatten(), 1)
nuclear_trendline = nuclear_slope * nuclear_capacity + nuclear_intercept

gas_capacity = gas_data['capacity_mw'].values.reshape(-1, 1)
gas_generation = gas_data['2019'].values.reshape(-1, 1)
gas_slope, gas_intercept = np.polyfit(gas_capacity.flatten(), gas_generation.flatten(), 1)
gas_trendline = gas_slope * gas_capacity + gas_intercept

plt.plot(nuclear_capacity, nuclear_trendline, color='red', label='Nuclear Trend Line')
plt.plot(gas_capacity, gas_trendline, color='blue', label='Gas Trend Line')

plt.xlabel('Capacity (MW)')
plt.ylabel('Energy Generation (GWh)')
plt.title('Capacity vs. Generation by Fuel Type')
plt.legend()
plt.show()

selected_fuels = ['Hydro', 'Solar', 'Wind', 'Biomass', 'Geothermal']
gen_growth_filtered = gen_growth[gen_growth['primary_fuel'].isin(selected_fuels)]

generation_by_fuel = gen_growth_filtered.groupby('primary_fuel')[['2013', '2014', '2015', '2016', '2017', '2018',
                                                                  '2019']].sum()

generation_by_fuel = generation_by_fuel.transpose()

plt.plot(generation_by_fuel.index, generation_by_fuel.values)
plt.xlabel('Year')
plt.ylabel('Total in Energy Generation(GWh)')
plt.title('Change in Energy Generation in the US (2013-2019) by Fuel Type')
plt.legend(generation_by_fuel.columns)
plt.xticks(rotation=90)
plt.show()
