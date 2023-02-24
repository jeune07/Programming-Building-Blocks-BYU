# How large is the loan?

# How good is your credit history?

# How high is your income?

# How large is your down payment?


loanScore=float(input("How large is the loan?"))
creditHistory=float(input("How good is your credit history?"))
income=float(input("How high is your income?"))
downPayment=float(input("How large is your down payment?"))

if loanScore>=5:
    if creditHistory>=7 and income>=7:
        decision="Yes"
    elif creditHistory>=7 or income>=7:
            if downPayment>=5:
               decision="Yes"
            else:
              decision="NO"
    else:
        decision="NO"  
else:
    if creditHistory<4:
       decision="NO"
    else: 
      if creditHistory>=7 or income>=7:
        decision="Yes"
      elif income>=4 and downPayment >=4:
        decision="Yes"
      else:
       decision="NO" 


print(decision)


