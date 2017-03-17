import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import heapq
from pylab import *

reader = open('criticReviews.csv',newline='')
csvReader = csv.reader(reader)
headers = next(csvReader)

movieName = input("Enter movie name to view critic review number \n")
movieName = movieName.strip()
movieName = movieName.lower()

flag = 0
numerOfReviews = 0
for row in csvReader:
    if movieName == row[11].strip().lower():
        numerOfReviews = row[2]
        print("Number of critic reviews for a movie are: ",numerOfReviews)
        flag = 1
        break
if flag == 0:
    print("Movie not found")

totalReviews = 0
criticList = []
reader.seek((0))
next(csvReader)
for values in csvReader:
     totalReviews = totalReviews + int(values[2])
     criticList.append(int(values[2]))

percentage = (int(numerOfReviews)/totalReviews) * 100
topFive = heapq.nlargest(5, criticList)
print("Top 5 number of critic reviews are: ",topFive)
labels = []
topFive.append(int(numerOfReviews))
labels = ["Top", "Two", "Three", "Four", "Five", movieName]
#print(labels)
sizes = topFive
explode = (0, 0, 0, 0, 0, 0.1)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()