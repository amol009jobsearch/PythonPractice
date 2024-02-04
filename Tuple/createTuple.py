'''
Tuple is like struct it can hold the multiple datatypes
Tuple is immutable i.e we cananot add,remove elements in tuple
Eventhough it is immutable we have hacks to add elements into tuple
'''

colorTuple=("Red","Green","Yellow")

print("type = ",type(colorTuple))

print("before deleting the tuple = ",colorTuple)

del colorTuple[1]

print("After deleting the tuple = ",colorTuple)