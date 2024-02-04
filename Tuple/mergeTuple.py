citiesTuple=("pune","mumbai","pune")
print(citiesTuple.count("pune")) #count how many time the value comes in tuple

stateTuple=("maharashtra","goa","MP")

netuple=citiesTuple + stateTuple
print("newTuple = ",netuple)

netuple=citiesTuple[:2] + stateTuple[0:]
print("newTuple = ",netuple)