import EmailGroup
import matplotlib.pyplot as plt
import csv
import math
import Email

class Model:

    # constructor takes in 2 test datasets and processes the relavant data
    # associated with them using email and email group classes

    def __init__(self, spam, notSpam):
        self.nsGroup = EmailGroup.EmailGroup(notSpam)       #stores not spam email objects 
        self.sGroup = EmailGroup.EmailGroup(spam)           #stores spam email objects

        tokens = []
        tokens.extend(self.nsGroup.export())
        tokens.extend(self.sGroup.export())
        tokens = set(tokens)

        self.spamEmails = [Email.Email(email, self.classify(email)) for email in spam]
        self.nsEmails = [Email.Email(email, self.classify(email)) for email in notSpam]

        # for email in spam:
        #     self.spamEmails.append(Email.Email(tokens, email, self.classify(email)))

        # for email in notSpam:
        #     self.nsEmails.append(Email.Email(tokens, email, self.classify(email)))


        # self.coordinatesSpam = []
        # self.coordinatesNotSpam = []

        # datasets = [spam, notSpam]
        # storedIn = [self.coordinatesSpam, self.coordinatesNotSpam]
        
        # i = 0
        # for dataset in datasets:
        #     for email in dataset:             
        #         storedIn[i].append(self.classify(email))
        #     i += 1
    
    #   because more than 2 dimensions are used, we'll just use email 
    #   group distance from averagento represent an email graphically

    def graphDatapoints (self):

        datasets = [self.spamEmails, self.nsEmails]
        colors = ["red", "blue"]
        labels = ["spam", "not spam"]

        i = 0
        for dataset in datasets:
            xLists = []
            yLists = []
            for email in dataset:
                x,y = email.coordinate[0], email.coordinate[1]            
                xLists.append(x)
                yLists.append(y)

            plt.scatter(xLists, yLists, color=colors[i], label=labels[i])
            i += 1
            
        plt.xlabel("not spam distance")
        plt.ylabel("spam distance")
        plt.legend()
        plt.grid()
        plt.show()

    # Currently exports the coordinates of spam and not spam emails
    # @TODO add more functionality, very barebones

    def exportData (self):
        with open('cordinatesSpam.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
        writer.writerows([(x.coordinate[0], x.coordinate[1]) for x in self.spamEmails])
        
        with open('cordinatesNotSpam.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
        writer.writerows([(x.coordinate[0], x.coordinate[1]) for x in self.nsEmails])

    # PREDICT
    # uses k nearest neighbors to classify an email
    # also can plot and textually represent an email being classified

    def predict (self, email, plot = False, console = False):
        x, y = self.classify(email)
        spamDistances = [(point.distance(email), point) for point in self.spamEmails]
        hamDistances = [(point.distance(email), point) for point in self.nsEmails]
        
        all = []                     
        spamDistances.sort(key=lambda x: x[0])
        hamDistances.sort(key=lambda x: x[0])

        all.extend(spamDistances)
        all.extend(hamDistances)
        all.sort(key=lambda x: x[0])
        all = all[:5]
        
        score = 0
        line = ""
        xListS = []
        yListS = []
        xListNS = []
        yListNS = []

        # finding where each email belons in their set
        for element in all:
            if element in hamDistances:
                score += 1
                line = line + "ns " 
                xListNS.append(element[1].coordinate[0])
                yListNS.append(element[1].coordinate[1])

            elif element in spamDistances:
                score -= 1
                line = line + "s "
                xListS.append(element[1].coordinate[0])
                yListS.append(element[1].coordinate[1])

            line = line + str(element[1].coordinate) + " "+ str(element) + "\n"
        
        if plot:
            plt.plot(x,y,'go') 
            plt.scatter(xListS, yListS, color='red', label='spam')
            plt.scatter(xListNS, yListNS, color='blue', label='not spam')
            plt.show()

        if console:
            print("( " + str(x) + " , " + str(y) + " )")
            print (str(score) + "\n" + line)

        if (score > 0):
            return False
        elif (score <= 0):
            return True
        
    def classify (self, email):
        return self.nsGroup.distance(email), self.sGroup.distance(email)