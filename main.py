import pandas as pd
import matplotlib.pyplot as plt


# Topic: Fertility rates and their decrease over the decades
data = pd.read_csv('children-per-woman-UN.csv', usecols=[0, 2, 3])
# print(data.describe())

us_data = data[data['Entity'] == 'United States']

us_data.plot(x='Year', y='Estimates 1950 - 2015: Demographic Indicators - Total fertility (live births per woman)', kind='scatter')

plt.xlabel("Years (1950 - 2015)")
plt.ylabel("# of children per woman")
plt.title("UN Fertility Data: # of children per woman over time")
plt.savefig('fertility-rate-united-states.png')
plt.show()
