personDetails={
    "name":"Amol",
    "surname":"randive",
    "age":33,
    "Mobile":7798823525
}

print("type = ",type(personDetails))

print("access elements = ")

for i in personDetails:
    print("each element = ",personDetails[i])

for i in personDetails.keys():
    print("keys = ",i)

for i in personDetails.values():
    print("values = ",i)

for key,value in personDetails.items():
    print("key = ",key)
    print("values = ", value)