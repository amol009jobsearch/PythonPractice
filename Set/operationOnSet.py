#add elements in set
citySet={"pune","mumbai"}
print("before adding elements in citySet = ",citySet)
citySet.add("nashik")
print("After adding elements in citySet = ",citySet)

stateSet={"Maharashtra","Goa"}

citySet.update(stateSet)
print("After updating elements in citySet = ",citySet)
numberSet={1,2}
unio_city_number=citySet.union(numberSet)
print("After union elements in citySet = ",unio_city_number)


