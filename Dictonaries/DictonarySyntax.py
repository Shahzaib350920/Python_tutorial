#Dictonary

info = {
    "key":"value",
    "Name":"Shaheryar Akhtar",
    "Age":19,
    "Sex":"Male",
    "City":"Karachi",
    "Country":"Pakistan"
}

print(info["City"])
print(info["Age"])
print(info["Name"])
print(info)


#Nested Dictonsary

info2 = {
    "key":"value",
    "Name":"Shaheryar Akhtar",
    "Age":20,
    "City":"Karachi",
    "Country":"Pakistan",
    "Fav Movies":{
        "Movie1":"Inception",
        "Movie2":"Interstellar",
        "Movie3":"3 Idiots"
    },
    "Fav Songs":{
        "Song1":"See You Again",
        "Song2":"Let Me Love You",
        "Song3":"Faded"
    }
}

#Accessing Nested Dictonary

print(info2["Fav Movies"]["Movie1"])
print(info2["Fav Songs"]["Song3"])
print(info2)

#Methids in Dictonary


info.keys()      #Gives all the keys in the dictonary
info.values()    #Gives all the values in the dictonary
info.items()     #Gives all the items in the dictonary in tuple form
info.clear()     #Clears the dictonary
info.copy()      #Copies the dictonary
info.get("Name")   #Gives the value of the key mentioned
info.pop("Age")    #Removes the item with the key mentioned
info.update({"Age":19})  #Updates the value of the key mentioned