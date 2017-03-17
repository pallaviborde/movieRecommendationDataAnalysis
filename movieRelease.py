import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt

reader = open('movieRelease.csv',newline='')
csvReader = csv.reader(reader)
headers = next(csvReader)

dict = {}
key = ''
count = 0
for row in csvReader:
    #print(row[23])
    key = row[23]
    #print(key)
    if key in dict:
        dict[key] = dict[key] + 1
    else:
        dict[key] = count + 1
x = sorted(list(dict.keys()))
y = sorted(list(dict.values()))
#print(type(y))
plt.plot(x,y)
plt.show()