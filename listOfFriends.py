# Ask the user for the names of their friends and append them to a list. Then, display each of the 
# friends in the list. You should stop asking for friends when the user types "end".


friendsList=[]
frindName =""


while frindName != "end":
    frindName=input("what are the of your friends ")
    friendsList.append(frindName)
for friend in friendsList:
    print(friend)
    print(friendsList)