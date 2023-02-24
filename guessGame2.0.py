print("Welcome to the word guessing game!")
secretword = "secret"
tryCount = 0
hint = ""
letterUnder = ""
message = ""


while True:
    userword = input("Enter your guess: ")  
    tryCount +=1
    hint = ""
    letterUnder = ""
    message = ""
    
    
    if secretword == userword:
        message = "Congratulations! You guessed it!"
        print(message)
        print(tryCount)
        break
    while len(secretword) == len(userword):
        for i in range(len(secretword)):
            if secretword[i] in userword:
                if secretword[i] == userword[i]:
                 hint += secretword[i].upper()
                 tryCount += 1
                 print("Your hint is: tttt" + hint)
        
    # for i in range(len(secretword)):
    #     if secretword[i] in userword:
    #         if secretword[i] == userword[i]:
    #             hint += secretword[i].upper()
    #             tryCount += 1
    #         else:
    #             hint += secretword[i].lower()
    #             tryCount += 1
    #     else:
    #         hint += "_"
    print("Your hint is: " + hint)
print(f"You have tried {tryCount} times.")





