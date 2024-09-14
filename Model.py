import EmailGroup
import matplotlib.pyplot as plt

class Model:
    #   constructor reads in csv file
    def __init__(self, spam, notSpam, testSpam, testNotSpam):
        self.spam = spam
        self.notSpam = notSpam
        self.testSpam = testSpam
        self.testNotSpam = testNotSpam

        self.nsGroup = EmailGroup.EmailGroup(self.notSpam)
        self.sGroup = EmailGroup.EmailGroup(self.spam)
    
    #   because more than 2 dimensions are used, we'll just use email 
    #   group distance to represent an email graphically
    def graphDatapoints (self):

        #oh dear...
        nsSpamList = list()
        sSpamList = list()
        sNotSpamList = list()
        nsNotSpamList = list()    
        nsTestSpam = list()
        sTestSpam = list()
        nsTestNotSpam = list()
        sTestNotSpam = list()

        xLists = [nsSpamList, nsNotSpamList, nsTestSpam, nsTestNotSpam]
        yLists = [sSpamList, sNotSpamList, sTestSpam, sTestNotSpam]
        datasets = [self.spam, self.notSpam, self.testSpam, self.testNotSpam]
        colors = ["red", "blue", "orange", "purple"]
        labels = ["not spam", "spam", "test spam", "test not spam"]

        i = 0
        for set in datasets:
            for email in set:
                
                xLists[i].append(self.nsGroup.distance(email))
                yLists[i].append(self.sGroup.distance(email))

            plt.scatter(xLists[i], yLists[i], color=colors[i], label=labels[i])
            i += 1
            

        plt.xlabel("not spam distance")
        plt.ylabel("spam distance")
        plt.legend()
        plt.grid()
        plt.show()