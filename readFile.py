try:
    with open("Users/Arbusta/Downloads/books.txt") as books:
        for book in books:
            print("book")

except FileNotFoundError :
    print("I an open the file")
except Exception as e:
    print("enesperate erroo", str(e))


print("what is that")

















# with open("Users/Arbusta/Downloads/books.txt") as books:
#     for book in books:
#         print(book)