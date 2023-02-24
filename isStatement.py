# What is the first number? 4
# What is the second number? 3
# The first number is greater
# The numbers are not equal
# The second number is not greater

# What is your favorite animal? giraffe
# That one is not my favorite.

firstNUmber= input("What is the first number?")
firstNUmber=int(firstNUmber)
secondNumber= input("What is the second number?")
secondNumber=int(secondNumber)

if firstNUmber> secondNumber:
    print("The first number is greater")
    print("The numbers are not equal")

elif firstNUmber< secondNumber:
    print("The first number is not greater")
    print("The numbers are not equal")
    print("The second number is greater")
else:
    print("entro aca")

favoriteAnimal=input("What is your favorite animal?")
favoriteAnimal=favoriteAnimal.lower()

if favoriteAnimal=="cat":
    print("That's my favorite animal too!")
else:
    print("TThat one is not my favorite")
