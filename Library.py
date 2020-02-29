class Library:

    books = []
    totalScore = 0
    def __init__(self, id, signUpTime, numBooks, scanningLimit):
        self.id = id
        self.signUpTime = signUpTime
        self.numBooks = numBooks
        self.scanningLimit = scanningLimit
        self.books.clear()

    def addBook(self, book):
        self.books.append(book)
        self.totalScore += book.score
        self.books.sort(key=self.sortBooks, reverse=True)

    def sortBooks(self, book):
        return book.score


    def toString(self):
        print("Library", self.id, "have", self.numBooks, "books, It needs",
              self.signUpTime, " days to SignUp and it can scan",
              self.scanningLimit, "books per day")
        print("Total Score for this Library is", self.totalScore)
        for b in self.books:
            b.toString()
        print("###############################")