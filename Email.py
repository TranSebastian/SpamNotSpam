class Email:

    # constructor takes in the list of words to look for, the email
    # and the coordinate associated with the email produced by email group

    def __init__(self, email, coordinate):
        
        self.coordinate = coordinate        # helpful to store coordinate here for easy graphing
        self.wordCount = dict()             # stores the relavant counts of words provided by email group
        for index in email.split(" "):
            if index in self.wordCount:
                self.wordCount[index] += 1
            else:
                self.wordCount[index] = 1
    
    # DISTANCE
    # distance takes in a email string and turns it into a dictionary
    # with its word counts. Then it calculates distance from this email
    # @TODO: pass email in a dictionary because recalculating it EVERY time is odd

    def distance (self, email):
        temp = dict()
        for index in email.split(" "):
            if index in temp:
                temp[index] += 1.0
            else:
                temp[index] = 1.0

        total = 0
        for key in self.wordCount:
            if key in temp:
                total += (temp[key] - self.wordCount[key])**2
            else:
                total += (self.wordCount[key])**2

        for key in temp:
            if key not in self.wordCount:
                total += temp[key]**2
        
        return total**(1/2)


        