import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
df = pd.read_csv('Team_Records.csv', delimiter = ',').fillna(0)

df=df[df.ORtg>0]
df = df[df.Season!='2017-18']
ORating = df.Rel_ORtg
DRating = df.Rel_DRtg
plt.scatter(ORating,DRating)

Wins = df.W
plt.scatter(ORating,Wins)
plt.xlabel('Offensive Rating')
plt.ylabel('Wins')
plt.annotate('Warriors 2016', xy=(8.2,73), xytext=(10, 90),arrowprops=dict(facecolor='red', shrink=0.05))
stats = linregress(ORating, Wins)
m = stats.slope
b = stats.intercept
plt.plot(ORating, m*ORating+b,color = 'red')

spurs_indeces = df.Team == ('San Antonio Spurs*')
spurs_indexes = df.Team == ('San Antonio Spurs')
spurs_indeces = spurs_indeces | spurs_indexes
plt.plot(DRating[~spurs_indeces],Wins[~spurs_indeces],'ro')
plt.plot(DRating[spurs_indeces],Wins[spurs_indeces],'gs')
#plt.plot(DRating[spurs_indexes],Wins[spurs_indexes],'gs')
plt.xlabel('Defensive Rating')
plt.ylabel('Wins')
stats = linregress(DRating[spurs_indeces], Wins[spurs_indeces])
m = stats.slope
b = stats.intercept
plt.plot(ORating, m*ORating+b,color = 'blue')
