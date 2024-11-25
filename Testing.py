import sys
import csv
import Model
import random

maxInt = sys.maxsize    
while True:
    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

# read file and extract emails
with open('spam_or_not_spam.csv', mode ='r', encoding="utf8") as file:  
    dataset = csv.reader(file)
    next(dataset, None) #clear headers

    spam = list()
    notSpam = list()
    testSpam = list()
    testNotSpam = list()

    var = 0
    for line in dataset:
        #training data
        if (line[1] == '0' and len(notSpam) < 250 and var % 10 == 0):
            notSpam.append(line[0])
        elif (line[1] == '1' and len(spam) < 250 and var % 2 == 0):
            spam.append(line[0])

        #testing data
        elif (line[1] == '0' and len(testNotSpam) < 250):
            testNotSpam.append(line[0])
        elif (line[1] == '1'):
            testSpam.append(line[0])

        var += 1

print("done adding emails!")

test= Model.Model(spam, notSpam)

correctHam = 0
for email in testNotSpam:
    if (not test.predict(email, False, False)):
        correctHam += 1

print("getting there!")

correctSpam = 0
for email in testSpam:
    if (test.predict(email, False, False)):
        correctSpam += 1

print(correctHam/len(testNotSpam))

print(correctSpam/len(testSpam))

print((correctHam + correctSpam) / (len(testSpam) + len(testNotSpam)))

#test.exportData()
test.graphDatapoints()
