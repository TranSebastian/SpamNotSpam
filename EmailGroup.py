import math

class EmailGroup:
    #constructor, takes in a group of emails
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
            self.emailCount[word] = temp[word] 

    #calculates euclidean distance from this email group
    def distance (self, email):
       
       #create dictionary
        temp = dict()
        for word in email.split(" "):              
            if (word in temp): 
                temp[word] += 1
            else:
                temp[word] = 1.0

        # euclidean distance
        num = 0
        for key in self.emailCount:
            if (key in temp):
                num += math.pow(self.emailCount[key] - temp[key], 2)
            else:
                num += math.pow(self.emailCount[key], 2)

        num = math.sqrt(num)
        return num

