'''Write a NumPy program to display all the dates for the month of March, 2017'''
import numpy as np

# Create a NumPy array with dates for the month of March 2017
dates_march_2017 = np.arange('2017-03-01', '2017-04-01', dtype='datetime64[D]')

print("Dates for the month of March 2017:")
print(dates_march_2017)