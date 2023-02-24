
print("Welcome to meal calculator")

childrenMeal=input("What is the price of a child's meal? ")
childrenMeal=float(childrenMeal)
adultMeal=input("What is the price of an adult's meal? ")
adultMeal= float(adultMeal)
childrenumber=input("How many children are there? ")
childrenumber =int(childrenumber)
adultnumber=input("How many children are there? ")
adultnumber =int(adultnumber)
tax=input("What is the sales tax rate? ")
tax =float(tax)/100

totalChildrenMeal=childrenMeal * childrenumber
totalAdulMeal=adultMeal * adultnumber
subTotal=totalChildrenMeal + totalAdulMeal
salesTax=tax * subTotal
total= salesTax + subTotal

print("SubTotal is : " + str(subTotal))
print("Sales Tax : " + str(salesTax))


payment =input("What is the payment amount?")
payment= int(payment)

if payment >= total:
    change=payment-total
    print("change is : "+ str(change))
else:
    print("The payment may be superior or igual to the total")