class Book:
    def __init__(self, name, author, price, publishing_year):
        self.book_name = name
        self.book_author= author
        self.book_price = price
        self.book_pd = publishing_year
        
    def add_books(self):
        print("Name:"+self.book_name)
        print("Author:"+str(self.book_author))
        print("Price:"+self.book_price)
        print("Publishing year:"+self.book_pd)
        print("book added")
        
        
book1 =Book("The Puffin History","Roshen Dalal","₹334","15 feb 2014")        
book1.add_books()

book2 =Book("Daddy long Legs","Jean Webster","₹144","1912")        
book2.add_books()

book3 =Book("Secret Garden","Frances Hodgson Burnett","₹124","1911")        
book3.add_books()

book4 =Book("What Katy Did","Sarah Chauncey Woolsey","₹440","1872")        
book4.add_books()

book5 =Book("Why am i an Atheist","Bhagat Singh","₹98","1930")        
book5.add_books()

book6 =Book("Shiva Triology (all III parts)","Amish Patel","₹729","1 Jan 2015")        
book6.add_books()