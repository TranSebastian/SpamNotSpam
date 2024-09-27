import EmailGroup
import matplotlib.pyplot as plt
import csv

class Model:
    #   constructor reads takes in 2 datasets
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
                storedIn[i].append((self.nsGroup.distance(email), self.sGroup.distance(email)))
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

        nsDistance = list()
        sDistance = list()
        distances = [nsDistance, sDistance]
        coordinates = [self.coordinatesNotSpam, self.coordinatesSpam]
        x = 0
        
        for coord in coordinates:
            for point in coord:
                var = (x - point[0])**2 + (y - point[1])**2
                distances[x].append(var ** (1/2))
            distances[x].sort()
            distances[x] = distances[x][:7]
            x += 1

        neighborS = set()
        neighborNS = set()
        for distance in nsDistance :
            for compare in sDistance :
                if (distance < compare):
                    neighborNS.add(distance)
                else:
                    neighborS.add(compare)
    
        if (len(neighborNS) > len(neighborS)):
            return False
        else:
            return True
        
