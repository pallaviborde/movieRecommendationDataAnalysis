import csv
import pandas as pd
import numpy as np
#import pandas as pd
import csv
#import numpy as np
import matplotlib.pyplot as plt
import heapq

csvReader = csv.reader(open('movie_metadata.csv'), delimiter=',')
headers = next(csvReader)  # list of headers

with open('criticProcess.csv', 'w', newline='') as csvFile:

    csvWriter = csv.writer(csvFile, delimiter=',')
    csvWriter.writerow(headers)
    for row in csvReader:
        try:
            if row[2]:
                    # print(row[5])
                csvWriter.writerow(row)
        except:
            continue
