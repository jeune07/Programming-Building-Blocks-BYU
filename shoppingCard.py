articleList=[]
priceList=[]
arcticle=None
price=None
userchoice=None
removeItem=None
total=0

while arcticle != "end":
    print("""
        Please select one of the following: 
        1. Add item
        2. View cart
        3. Remove item
        4. Compute total
        5. Quit
        """)
    userchoice=input("Please enter an action:")
    if userchoice =="1":
        arcticle = input("What item would you like to add?")
        
        if arcticle == "end":
         break
        else:
            price=input(f" What is the price of '{arcticle}'?")
            price = float(price)
            articleList.append(arcticle)
            priceList.append(price)
            print(f"{arcticle} has been added to the cart")
    elif userchoice=="2":
        for index in range(len(articleList)):
            print(f"{index+1}- {articleList[index]} {priceList[index]}")    

    elif userchoice=="3":
        removeItem=input("Which item would you like to remove?")
        removeItem= int(removeItem) -1
        del articleList[removeItem]
        del priceList[removeItem]
    
    elif userchoice=="4":
        for i in priceList:
            total += i
            print(f" The toal is {total}")
    elif userchoice=="5":
        print("thank you for using our program")
        break



