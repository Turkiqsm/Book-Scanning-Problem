class Book(object):

    def __init__ (self, id, score):
        self.id = id
        self.score = score

    def getScore(self):
        return self.score

    def toString(self):
        print("Book ", self.id , " has a score of", self.score)