import EmailGroup
import matplotlib.pyplot as plt
import csv
import math

class Model:
    #   constructor takes in 2 datasets
    def __init__(self, spam, notSpam):
        self.nsGroup = EmailGroup.EmailGroup(notSpam)
        self.sGroup = EmailGroup.EmailGroup(spam)

        self.coordinatesSpam = []
        self.coordinatesNotSpam = []

        datasets = [spam, notSpam]
        storedIn = [self.coordinatesSpam, self.coordinatesNotSpam]
        
        i = 0
        for dataset in datasets:
            for email in dataset:             
                storedIn[i].append([self.nsGroup.distance(email), self.sGroup.distance(email)])
            i += 1
    
    #   because more than 2 dimensions are used, we'll just use email 
    #   group distance to represent an email graphically
    def graphDatapoints (self):

        datasets = [self.coordinatesSpam, self.coordinatesNotSpam]
        colors = ["red", "blue"]
        labels = ["spam", "not spam"]

        i = 0
        for dataset in datasets:
            xLists = []
            yLists = []
            for email in dataset:             
                xLists.append(email[0])
                yLists.append(email[1])

            plt.scatter(xLists, yLists, color=colors[i], label=labels[i])
            i += 1
            
        plt.xlabel("not spam distance")
        plt.ylabel("spam distance")
        plt.legend()
        plt.grid()
        plt.show()

    def exportData (self):
        with open('cordinatesSpam.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(self.coordinatesSpam)
        
        with open('cordinatesNotSpam.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(self.coordinatesNotSpam)
    
    def predict (self, email):
        x = self.nsGroup.distance(email)
        y = self.sGroup.distance(email)
        print("( " + str(x) + " , " + str(y) + " )")
        plt.plot(x,y,'go') 

        spamDistances = []
        hamDistances = []
        all = []
        coords = dict()

        for point in self.coordinatesNotSpam:
            var = math.dist(point, [x,y])
            hamDistances.append(var)
            coords[var] = point
        
        for point in self.coordinatesSpam:
            var = math.dist(point, [x,y])
            spamDistances.append(var)
            coords[var] = point
            
        spamDistances.sort()
        hamDistances.sort()

        all.extend(spamDistances)
        all.extend(hamDistances)
        all.sort()
        all = all[:7]
        
        score = 0
        line = ""
        xListS = []
        yListS = []
        xListNS = []
        yListNS = []

        for element in all:
            if element in hamDistances:
                score += 1
                line = line + "ns " 
                xListNS.append(coords[element][0])
                yListNS.append(coords[element][1])

            elif element in spamDistances:
                score -= 1
                line = line + "s "
                xListS.append(coords[element][0])
                yListS.append(coords[element][1])

            line = line + str(coords[element]) + " "+ str(element) + "\n"
        print (str(score) + "\n" + line)
        plt.scatter(xListS, yListS, color='red', label='spam')
        plt.scatter(xListNS, yListNS, color='blue', label='not spam')
        plt.show()

        if (score > 0):
            return False
        if (score <= 0):
            return True