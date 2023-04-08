def main():
    # Create a dictionary with student IDs as
    # the keys and student names as the values.
    students_dict = {
        "42-039-4736": "Clint Huish",
        "61-315-0160": "Amelia Davis",
        "10-450-1203": "Ana Soares",
        "75-421-2310": "Abdul Ali",
        "07-103-5621": "Amelia Davis"
    }

    # add an item to the dictionary

    students_dict["07-103-5638"]="jeune winsley"

    #Remove an item from the dictionary

    students_dict.pop("07-103-5638")

    #get the number of item in the dictionary

    length= len(students_dict)


    #get a student id from the user

    studentID=input("Enter a student id:")
    if studentID in students_dict:
        name= students_dict[studentID]
        print(name)

if __name__ == "__main__":
    main()