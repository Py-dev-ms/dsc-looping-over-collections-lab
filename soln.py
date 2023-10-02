import pandas as pd
import matplotlib.pyplot as plt

# %matplotlib inline

file_name = './cities.xlsx'
travel_df = pd.read_excel(file_name)
cities = travel_df.to_dict('records')
city_names = []
names_and_ranks = []
city_populations = []
city_areas = []

city_indices = list(range(0, len(cities)))
# print(city_indices)

buenos_aires = cities[0]['City']
# print(buenos_aires)

for city in city_indices:
    city_names.append(cities[city]['City'])

# print(city_names)


for city in city_indices:
    # city_indices[city] += 1
    names_and_ranks.append(f'{city+1}. {cities[city]["City"]}')

# print(names_and_ranks)

for city in city_indices:
    # city_populations.append(f'{cities[city]["City"]} Population: {cities[city]["Population"]}')
    city_populations.append(cities[city]["Population"])

# print(city_populations)

# plt.bar(names_and_ranks, city_populations)
# plt.xticks(rotation='vertical')
# plt.ylabel('Population')
# plt.title('City Populations')
# plt.show()

# plt.bar(names_and_ranks, city_populations)

# plt.ylabel('Population')
# plt.xlabel('Cities')
# plt.title('City Populations')
# plt.xticks(rotation='vertical')
 
# plt.show()


for city in city_indices:
    # city_areas.append(f'{cities[city]["City"]} Area: {cities[city]["Area"]}')
    city_areas.append(cities[city]["Area"])

plt.bar(names_and_ranks, city_areas)
plt.ylabel('Area')
plt.xlabel('Cities')
plt.title('City Areas')
plt.xticks(rotation='vertical')
 
plt.show()

# for city in list(range(0, 4)):
#     print("City Name: ", cities[city])

    
# x_values = [cities[0]['City'], cities[1]['City'], cities[2]['City']]
# y_values = [cities[0]['Population'], cities[1]['Population'], cities[2]['Population']]
 
# plt.bar(x_values, y_values)
# plt.ylabel('Population')
# plt.title('City Populations')
 
# plt.show()
