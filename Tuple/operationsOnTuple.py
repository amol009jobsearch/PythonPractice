stateTuples=("India",)
#convert tuple to list

stateList=list(stateTuples)
stateList.append("UK")
stateList.append("Nepal")
stateList.append("Shrilanka")

stateTuples=tuple(stateList)
print("stateTuples = ",stateTuples)

print("know item exist in tuple = ","UK" in stateTuples)

#unpack tuple items

country1,country2,country3,country4 = stateTuples

print("country1 = ",country1)
print("country2 = ",country2)
print("country3 = ",country3)
print("country4 = ",country4)

newTuple=country1,country2,country3,country4
print("newTuple = ",newTuple)


tuplex=(1,"Amol",[],33)
print(type(tuplex[2]))

tuplex[2].extend(["Maths","MCA"])

print(tuplex)