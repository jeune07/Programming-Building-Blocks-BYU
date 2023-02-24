


# m = mass (in kg)

# g = acceleration due to gravity (9.8 m/s^2 on Earth, 24 m/s^2 on Jupiter)

# t = time (in seconds)

# c = 1/2 p A C

# p = density of fluid (1.3 kg/m^3 for air, 1000 kg/m^3 for water)

# A = cross sectional area of projectile (in square meters)

# C = drag constant (0.5 for sphere, 1.1 for cylinder falling on it’s side. You could look it up for other shapes.)

# exp = the number e (2.71828) to the given exponent. This can be computed in Python with the Math library function math.exp(value).

# sqrt = the square root of the given expression. This can be computed in Python with the Math library function math.sqrt(value).

import math

print("welcome to the best velocity calculator")

m=input("Enter the mass in kg")
m=float(m)
g=input("Enter the gravity remember is 9.8 m/s^2 on Earth and  24 m/s^2 on Jupiter ")
g=float(g)
t=input("Enter the time in seconds")
t=int(t)
p=input("Enter the density of fluid (1.3 kg/m^3 for air, 1000 kg/m^3 for water)")
p=float(p)
A=input("Enter the cross sectional area of projectile (in square meters)")
A=float(A)
C=input("Enter drag constant (0.5 for sphere, 1.1 for cylinder )")
C=float(C)
e =print("We asume that e is 2.71828")
c=0.5*p*A*C
crounded=round(c, 3)
#print(c)
printedValue=f"The inner value of c is: { crounded }"
print(printedValue)

sqrtmgc=math.sqrt(m*g*c)
mg_c=(m*g)/c

v=(math.sqrt(mg_c)) * (1-(math.exp((-math.sqrt(m*g*c)/m)*t)))
vRounded=round(v,3)
print(f"The velocity after {t} seconds is: {vRounded}")
print(v)