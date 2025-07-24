import pandas as pd
flight=pd.read_csv("flight.csv")
#print(flight)
#print(flight.head(10))
#print(flight.tail(10))
#print(flight.info())
print(flight.describe())
#print(flight.corr())
