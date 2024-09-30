import math
from nltk.corpus import stopwords

class EmailGroup:

    # constructor, takes in a group of emails and processes them
    
    def __init__(self, emailList):
        self.emailCount = dict()            #stores the word with the average count per email
        sw = stopwords.words('english')     #contains stopwords provided by nltk
        removables = []                     #will store the words we are actually looking to remove

        #modifying the stop words to remove apostrophes
        for token in sw: 
            index = token.find("'")
            if index != -1:
                removables.append(token[0:index] + token[index+1:len(token)])
            else:
                removables.append(token)
                
        #go through each email and process text
        for email in emailList:    
            words = email.split(" ")
            tokenizedText = []
            for word in words:      #turning text into tokens
                if word not in removables:
                    tokenizedText.append(word)

            #get word counts
            for word in tokenizedText:              
                if (word in self.emailCount):    #determine if word exists
                    self.emailCount[word] += 1
                else:
                    self.emailCount[word] = 1.0

        # get averages and place signifcant words into field dictionary
        for word in self.emailCount:
            self.emailCount[word] /= len(emailList)

    # provides the list of relavant words from this email group
    def export (self):
        keywords = list()
        for key in self.emailCount:
            keywords.append(key)
        return keywords        

    # DISTANCE
    # calculates euclidean distance from this email group as an average
    # @TODO also better email to have email as a dictionary for faster processing

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

