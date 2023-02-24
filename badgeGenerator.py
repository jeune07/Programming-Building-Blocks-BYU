

print("Please enter the following information")

firstName= input("Enter the First name: ").upper()
lastName= input("Enter the Last name: ").capitalize()
email= input("Enter a valid email: ")
phoneNumber=input("Enter your phone number: ")
jodtible=input("Enter your job title: ")
idNumber=input("Enter your Id: ")
height=input("Enter your height: ")
bloodType=input("Enter your blood type:")
fullName = "{} {}".format(firstName.upper(), lastName.capitalize())

print("-----------------------------------------------")
print(fullName +"\n"+ jodtible.title()+ "\n"+ idNumber +"\n"+"\n"+ email +"\n"+ phoneNumber +"\n"+"\n"+ "Height: "+height.ljust(20)+ "Blood Type: "+ bloodType.upper())
