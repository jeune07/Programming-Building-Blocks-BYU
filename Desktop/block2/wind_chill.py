tem = float(input("What is the temperature? "))
scale = input("Fahrenheit or Celsius (F/C)? ")

for v in range(5, 61, 5):
    if scale == "F":
        windchill = 35.74 + 0.6215 * tem - 35.75 * (v ** 0.16) + 0.4275 * tem * (v ** 0.16)
    else:
        temp_f = tem * 1.8 + 32
        windchill = 35.74 + 0.6215 * temp_f - 35.75 * (v ** 0.16) + 0.4275 * temp_f * (v ** 0.16)

    print(f"Windchill at {tem} {scale} and {v} mph is: {windchill:.2f}")
