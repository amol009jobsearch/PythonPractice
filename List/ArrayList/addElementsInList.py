colorList=["Yellow","Blue","Orange","Red"]

# print elements from list
print("print colorlist = ",colorList[1:3]) #list will start with 0th index
print("print colorlist = ",colorList[1:]) #list will start with 0th index
print("print colorlist = ",colorList[:3]) #list will start with 0th index

#add elements in list
colorList.insert(0,"Amol")
print(colorList)

#add elements in list at the end
colorList.insert(len(colorList),"LastElement")
print(colorList)

#append elements in list
colorList.append("Purple")
print("Append")
print(colorList)