books = ['English','Mathematics','Science','Programming','Story','SST']
copies = [18,12,23,5,16,0]
library = {book: i for book,i in zip(books,copies)}
print(library)
available_books = [book for book in books if library[book]!=0]
print("Books available: ",available_books)
book_to_borrow = input("What book do you wish to borrow")
if book_to_borrow not in library and library[book_to_borrow] == 0:
   print("Book not available")
   exit()


prices = [10,20,30,40,50,60]
late_fees = list(map(lambda x:x+5,prices))
count = 0
for late_fee in late_fees:
   print(f"{books[count]}'s Late Fees:$",late_fee)
   count+=1
   

library[book_to_borrow] -= 1
print(f"Stock after purchase:\n{library}")

print("Index of the chosen book: ",available_books.index(book_to_borrow))
print("=========")