
# grade= input("Please tell me your grade")
# grade=float(grade)

# if grade>= 90 and grade<=100:
#     print("your grade is A ")
# elif grade>= 80 and grade<90:
#     print("your grade is B ")
# elif grade>= 70 and grade<80:
#     print("your grade is C ")
# elif grade>= 60 and grade<70:
#     print("your grade is D ")
# else:
#     print("your grade is F ")

# if grade>70:
#     print("Good job you passed the course")
# else:
#     print("Sorry, you have not passed the course, you can try again.")

#-----------------------------------------------------------------------------------

grade= input("Please tell me your grade")
grade=float(grade)
if grade>= 90 and grade<=100:
    lettergrade="A"
    if grade>= 97 and grade<=100:
        gradeSing=""
    if grade>= 90 and grade<=97:
        gradeSing=""
elif grade>= 80 and grade<90:
    lettergrade="B"
elif grade>= 70 and grade<80:
    lettergrade="C"
    if grade>= 77 and grade<=80:
        gradeSing="+"
    if grade>= 70 and grade<77:
        gradeSing="-"
elif grade>= 60 and grade<70:
    lettergrade="D"
    if grade>= 67 and grade<=70:
        gradeSing="+"
    if grade>= 60 and grade<67:
        gradeSing="-"
else:
    lettergrade="F"
    gradeSing=""

print("your grade is " + lettergrade + gradeSing)


if grade>=70:
    print("Good job you passed the course")
else:
    print("Sorry, you have not passed the course, you can try again.")
