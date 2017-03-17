import csv
import pandas as pd
import numpy as np
#import pandas as pd
import csv
#import numpy as np
import matplotlib.pyplot as plt
import heapq



#function to preprocess data
def preprocessing():
    #read csv file
    csvReader = csv.reader(open('imdb.csv'), delimiter=',')
    headers = next(csvReader)  # list of headers
    #open new csv file to write
    with open('topProcess.csv', 'w', newline='') as csvFile:
        csvWriter = csv.writer(csvFile, delimiter=',')
        csvWriter.writerow(headers)
        for row in csvReader:
            try:
                #if values in column imdbRating is not integer or float remove that column
                if float(row[5]):
                    csvWriter.writerow(row)
            except:
                continue
#function to get top 10 movies
def top10Movies():
    df = pd.read_csv('topProcess.csv', usecols=['title', 'imdbRating'])
    top = df.sort_values(by='imdbRating', ascending=False).head(10)
    print(top)

#function to print which country watches which genre most
def genrePercentageCountry():

    csvReader = csv.reader(open('movie_metadata.csv', newline=''), delimiter=',')
    headers = next(csvReader)
    dict = {}
    count = 0
    key = ''
    for row in csvReader:
        #listOfGeneres is separated by '|'. Split it to make a list
        listOfGeneres = row[9].split('|')
        country = row[20]
        #create a dictionary data structure with key as country and genre and values with count of that genre
        for genres in listOfGeneres:
            # print(genres)
            key = country + ',' + genres
            # print(key)
            if key in dict:
                dict[key] = dict[key] + 1
            else:
                dict[key] = count + 1

    dictKeys = dict.keys()
    dictValues = dict.values()

    writeHeader = ['country', 'generes', 'count']
    #write this dictionary in csv file
    with open('dictGenre.csv', 'w', newline='') as csvFile:
        csvWriter = csv.writer(csvFile, delimiter=',')
        csvWriter.writerow(writeHeader)
        # rowWrite = []
        for k, v in dict.items():
            kSplit = k.split(',')
            kSplit.append(v)
            # print(kSplit)
            csvWriter.writerow(kSplit)
    #read csv file with pandas
    df = pd.read_csv('dictGenre.csv')

    idx = df.groupby(['country'])['count'].transform(max) == df['count']
    grp = df[idx]
    print(grp)
    a = df.groupby(['country'])[['country', 'count', 'generes']].sum().reset_index()

    #print(a)
    grpList = grp.values.T.tolist()
    aList = a.values.T.tolist()
    percentageList = []
    for i in range(0, len(grpList[0])):
        for j in range(0, len(aList)):
            if grpList[0][i] == aList[0][j]:
                percentage = (grpList[2][i] / aList[1][j]) * 100
                percentageList.append(percentage)

    x = grpList[1]


    N = len(x)
    ind = np.arange(N)
    y = percentageList
    # print(y)
    width = 0.35

    #plt.bar(ind + width, y, width, color='g')
    #plt.show()
#function to preprocess data which removes rows having critic recviews column null
def preProcessCritic():
    csvReader = csv.reader(open('movie_metadata.csv'), delimiter=',')
    headers = next(csvReader)  # list of headers
    #write in new csv file after deleting bad records
    with open('criticProcess.csv', 'w', newline='') as csvFile:
        csvWriter = csv.writer(csvFile, delimiter=',')
        csvWriter.writerow(headers)
        for row in csvReader:
            try:
                if row[2]:
                    csvWriter.writerow(row)
            except:
                continue

#function to show critic reviews of a movie
def criticReviews():
    reader = open('criticProcess.csv', newline='')
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
            print("Number of critic reviews for a movie are: ", numerOfReviews)
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

    percentage = (int(numerOfReviews) / totalReviews) * 100
    topFive = heapq.nlargest(5, criticList)
    print("Top 5 number of critic reviews are: ", topFive)
    labels = []
    topFive.append(int(numerOfReviews))
    labels = ["Top", "Two", "Three", "Four", "Five", movieName]
    # print(labels)
    sizes = topFive
    explode = (0, 0, 0, 0, 0, 0.1)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.savefig("criticPie.png")
    plt.show()

#preprocessing function to delete rows where year of release is null
def releasePreProcess():
    csvReader = csv.reader(open('movie_metadata.csv'), delimiter=',')
    headers = next(csvReader)  # list of headers
    with open('releaseProcess.csv', 'w', newline='') as csvFile:
        csvWriter = csv.writer(csvFile, delimiter=',')
        csvWriter.writerow(headers)
        for row in csvReader:
            try:
                if row[23]:
                    csvWriter.writerow(row)
            except:
                continue

#function to show how many movies released per year
def movieRelease():
    reader = open('releaseProcess.csv', newline='')
    csvReader = csv.reader(reader)
    headers = next(csvReader)
    dict = {}
    key = ''
    count = 0
    for row in csvReader:
        # print(row[23])
        key = row[23]
        # print(key)
        if key in dict:
            dict[key] = dict[key] + 1
        else:
            dict[key] = count + 1
    x = []
    y = []
    for key in dict:

        value = dict[key]
        key = int(key)
        v = int(value)
        x.append(key)
        y.append(v)

    plt.xlabel("Year")
    plt.ylabel("Number of movies released")


    plt.plot(x, y, "o")
    plt.savefig("movieReleased.png")
    plt.show()



if __name__ == '__main__':
    f = csv.writer(open("finalIMDB.csv","wb"))
    print("This application can perform following tasks. Please select one by entering number \n")
    choice = int(input("1. Top 10 movies by rating \n2. Which country watches which genre most \n"
                       "3. Number of critic reviews for a movie \n"
                       "4. How many movies released per year \n"))
    if choice == 1:
        preprocessing()
        top10Movies()
    if choice == 2:
        genrePercentageCountry()
    if choice == 3:
        preProcessCritic()
        criticReviews()
    if choice == 4:
        releasePreProcess()
        movieRelease()

