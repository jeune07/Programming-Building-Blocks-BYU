print("This program can help you write a funny story.")
continu = input(" Please press Y to continu or N to cancel: ")

if continu == "Y":
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    adverb = input("Enter an adverb: ")
    print("One day, I decided to " + verb +" to the store to buy a" +adjective +" "+ noun +". On my way there, I saw a " +adjective + " cat " 
    + adverb+ " climbing a tree.")
elif continu == "N":
    print("We are very sorry that you could not find this interesting.")
elif continu !="N" and continu !="Y":
    print("You need to enter Y or N please try again")

