import csv
import sys
import EmailGroup
import matplotlib.pyplot as plt

class Model:
    def __init__(self):
        # magic to get csv file to read.
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

            self.spam = list()
            self.notSpam = list()
            avgSpamLen = 0
            avgNSLen = 0

            var = 0
            for line in dataset:
                if (line[1] == '0' and len(self.notSpam) < 250 and var % 5 == 0):
                    self.notSpam.append(line[0])
                    avgNSLen += len(line[0])
                elif (line[1] == '1' and len(self.spam) < 250 and var % 2 == 0):
                    self.spam.append(line[0])
                    avgSpamLen += len(line[0])
                var += 1

        print(avgSpamLen/250)
        print(avgNSLen/250)
        self.nsGroup = EmailGroup.EmailGroup(self.notSpam)
        self.sGroup = EmailGroup.EmailGroup(self.spam)
        self.nsGroup.enhancePrecision(self.sGroup)
    
    #   because more than 2 dimensions are used, we'll just use email group distance
    #   to represent an email graphically
    def graphDatapoints (self):

        #spam data points
        nsSpamList = list()
        sSpamList = list()
        for email in self.spam:
            nsSpamList.append(self.nsGroup.distance(email))
            sSpamList.append(self.sGroup.distance(email))

        #not spam data
        sNotSpamList = list()
        nsNotSpamList = list()
        for email in self.notSpam:
            nsNotSpamList.append(self.nsGroup.distance(email))
            sNotSpamList.append(self.sGroup.distance(email))

        plt.scatter(nsSpamList, nsNotSpamList, color='blue', label="not spam")
        plt.scatter(sSpamList, sNotSpamList, color='red', label="spam")
        plt.legend()
        plt.show()


test = Model()
test.graphDatapoints()