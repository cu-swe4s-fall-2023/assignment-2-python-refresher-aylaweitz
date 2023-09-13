from my_utils import get_column

# print the number of fires in the United States of America
country='United States of America'
country_column = 0 # first column corresponds to the 0th index
fires_column = 3
file_name = 'Agrofood_co2_emission.csv'
fires = get_column(file_name, country_column, country, fires_column)
print(fires)
