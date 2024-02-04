personDetails={
    "name":"Amol",
    "surname":"randive",
    "age":33,
    "Mobile":7798823525
}

print("name = ",personDetails["name"])
print("age = ",personDetails["age"])
print("mobile = ",personDetails.get("Mobile"))
personDetails["Mobile"]=7030937144
print("mobile = ",personDetails.get("Mobile"))

print("keys = ",personDetails.keys())
print("values = ",personDetails.items())