
import math
from datetime import datetime

tire_width=input("Enter the width of the tire in mm (ex 205):")
tire_width =float(tire_width)
tire_aspect= input("Enter the aspect ratio of the tire (ex 60)")
tire_aspect =float(tire_aspect)
tire_dimenter=input("Enter the diameter of the wheel in inches (ex 15)")
tire_dimenter =float(tire_dimenter)
#v = π w2 aw a + 2,540 d/10,000,000,000
volumes=math.pi* tire_width**2 * tire_aspect*tire_width *tire_aspect + 2.540 * tire_dimenter/ 10000000000
today_date=datetime.now()

with open("./volumes.txt", "a") as volume:
    volume.write(f"At {today_date} the width is  {tire_width}, the aspect of ratio  is {tire_aspect}  the diameter of the wheel is {tire_dimenter} and the volume of the tire is {volumes}\n")

print(f"The approximate volume is {volumes} liters")
