
print("Welcome to the word guessing game!")
attempt = 0
hint = ""

while True:    
    secretword = "secret"
    userword = input("What is your guess? ")
    attempt += 1
    hint = ""
    
    if secretword == userword:
        print("Congratulations! You guessed it!")
        break
    elif len(secretword) == len(userword):
        for i in range(len(secretword)):
            if secretword[i] in userword:
                if secretword[i] == userword[i]:
                    hint += secretword[i].upper()
                else:
                    hint += secretword[i].lower()
            else:
                hint += "_"
    else:
        for i in range(len(secretword)):
            hint += "_"
    
    print("Your hint is: " + hint)

print(f"You took {attempt} attempts to guess the word.")