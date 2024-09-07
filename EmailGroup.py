import csv

class EmailGroup:
    def __init__(self, emailList):

        temp = dict()
        for email in emailList:
            words = email.split(" ")    #seperate email into words

            #get word counts
            for word in words:              

                if (word in temp):    #determine if word exists
                    temp[word] += 1
                else:
                    temp[word] = 1.0
        
        # get averages and place signifcant words into field dictionary
        self.emailCount = dict()
        for word in temp:
            temp[word] = temp[word]/len(emailList)

            if (temp[word] > 1):
                self.emailCount[word] = temp[word]
                #print(word + "\t" + str(self.emailCount[word]))

        #print (len(self.emailCount))
    
    def enhancePrecision (self, other):
        for key in other.emailCount:
            if (key in self.emailCount):

                selfVal = self.emailCount[key]
                otherVal = other.emailCount[key]
                self.emailCount[key] = selfVal - otherVal
                other.emailCount[key] = otherVal - selfVal

            else:
                self.emailCount[key] = 0

        for key in self.emailCount:
            if (key not in other.emailCount):
                other.emailCount[key] = 0

        print (len(self.emailCount))
        print (len(other.emailCount))

    def distance (self, email):
       
       #create dictionary
        temp = dict()
        for word in email.split(" "):              

            if (word in temp): 
                temp[word] += 1
            else:
                temp[word] = 1.0

        ## euclidean distance
        num = 0
        for key in self.emailCount:
            if (key in temp):
                num += ( self.emailCount[key] - temp[key] ) ** 2
            else:
                num += self.emailCount[key] ** 2

        num = num ** (1/2)
        print(num)
        return num

