# Please enter the items of the shopping list (type: quit to finish):
# Item: Milk
# Item: Bread
# Item: Candy
# Item: Carrots
# Item: quit




item =""

articleList = []
while item !="quit":
    item=input("Please enter the items of the shopping list (type: quit to finish):")
    if item !="quit":
        articleList.append(item)
       
for i in range(len(articleList)):
     print(f"{i}- {articleList[i]}")

