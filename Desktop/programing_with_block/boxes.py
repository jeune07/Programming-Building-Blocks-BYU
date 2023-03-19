import math
import datetime

box=float(input("Enter the number of items per box:"))
item=float(input("Enter the number of items:"))
boxes=math.ceil(box/item)
today_date=datetime.now()

print(f"For {box} items, packing {item} items in each box, you will need {boxes} boxes.")

