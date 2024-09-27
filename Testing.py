import sys
import csv
import Model

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
        elif (line[1] == '0' and len(testNotSpam) < 250 and var % 10 != 0):
            testNotSpam.append(line[0])
        elif (line[1] == '1'):
            testSpam.append(line[0])

        var += 1

test= Model.Model(spam, notSpam)
print("FUCK")
print(test.predict(testSpam[0]))
#test.exportData()
#test.graphDatapoints()
