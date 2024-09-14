import csv

class EmailGroup:
    #constructor, takes in a group of emails
    def __init__(self, emailList):
        avgLen = 0
        temp = dict()
        for email in emailList:
            words = email.split(" ")    #seperate email into words
            avgLen += len(email)

            #get word counts
            for word in words:              

                if (word in temp):    #determine if word exists
                    temp[word] += 1
                else:
                    temp[word] = 1.0
        avgLen /= len(emailList)  

        # get averages and place signifcant words into field dictionary
        self.emailCount = dict()
        for word in temp:
            temp[word] = temp[word]/avgLen
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

        ## euclidean distance
        num = 0
        for key in self.emailCount:
            if (key in temp):
                num += ( self.emailCount[key] - temp[key] ) ** 2
            else:
                num += self.emailCount[key] ** 2

        num = num ** (1/2)
        return num

