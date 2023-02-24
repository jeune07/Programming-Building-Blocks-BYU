

positiveNumber=float(input("Please type a positive number"))

while positiveNumber<0:
    positiveNumber=float(input("Please type a positive number"))

print(f"the number is {positiveNumber}")


answer=input("May I have a piece of candy")
answer=answer.upper()

while True:
    if answer=="YES":
     print("Thank you")
     
     break
         
    else:
        answer=input("May I have a piece of candy")
        answer=answer.upper()



