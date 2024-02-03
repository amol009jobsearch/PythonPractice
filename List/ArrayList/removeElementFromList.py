'''
There are below 3 ways by which we can remove the elements from list
  1) use pop method to remove the last element from list
  2) use remove method if you want to remove the element by its value
  3) use del method to delete the elements by its index
'''
colorList=["Yellow","Blue","Orange","Red"]

print("Before removing elements = ",colorList)
colorList.pop()
print("After removing elements = ",colorList)

#use the remove method to remove the elements by its value

colorList.remove("Yellow")
print("list after remove = ",colorList)

#remove/delete the elements of list by its index
del colorList[1]
print("list after del = ",colorList)
