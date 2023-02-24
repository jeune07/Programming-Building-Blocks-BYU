# (5 °F − 32) × 5/9 = -15 °C

temperatraFareneit=input("Enter a temperature un fareneit")




try: 
    temperatraFareneit =float(temperatraFareneit)

    
except:
    print("you can convert only a number")

else:
    conversionCelcius= (temperatraFareneit -32) * 5/9
    conversionCelcius =round(conversionCelcius, 1)

    print(conversionCelcius)
