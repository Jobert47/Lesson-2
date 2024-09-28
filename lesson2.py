age = [-12,13,-14,-16]

username = ["juan","pedro", "james","sagaad","fuego"]

for dataage in age:
    if dataage > 0:
        print (str(dataage) + "negative")
    elif dataage < 0:
        print (str(dataage) + "positive")
        
for datauser in username:
    if datauser == "james":
       print ("james cute")
    else:
        print ("james none")