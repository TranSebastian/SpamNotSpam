import csv
import sys
import EmailGroup

class Model:
    def __init__(self):
        # magic to get csv file to read. Java does this stuff better NO HATE!!
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
            var = 0
            for line in dataset:
                if (line[1] == '0' and len(notSpam) < 500 and var % 5 == 0):
                    notSpam.append(line[0])
                elif (line[1] == '1' and len(spam) < 500):
                    spam.append(line[0])
                var += 1

        self.nsGroup = EmailGroup.EmailGroup(notSpam)
        self.sGroup = EmailGroup.EmailGroup(spam)
        self.nsGroup.enhancePrecision(self.sGroup)

        self.nsGroup.distance(spam[0])
        self.sGroup.distance(spam[0])