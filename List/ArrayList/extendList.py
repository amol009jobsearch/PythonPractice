'''
We can extend(append) to the existing list

'''

colorList=["Red","Blue","Green"]
LatestColors=["Purple"]
numberList=[1,2,3]
tupleColors=("Yellow","Pink")
print("Before Extending the colorList = ",colorList)
colorList.extend(LatestColors)
print("After Extending the colorList = ",colorList)

print("Before Extending the numberList = ",colorList)
colorList.extend(numberList)
print("After Extending the numberList = ",colorList)

print("Before Extending the Tuple = ",colorList)
colorList.extend(tupleColors)
print("After Extending the Tuple = ",colorList)