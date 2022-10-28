# key - value pair

jediCouncil = {
    "Yoda": "Dagobah",
    "Obiwan": "Death Star",
    "Mace Windu": "Coruscant"
}
jediCouncil["Anakin"] = "Death Star"    # this adds the new item into the dictionary. 
print(jediCouncil)

# 2nd example

councilJedi = {
    1: {
        "name" : "Obiwan",
        "surname" : "Kenobi",
        "Death" : "Death Star",
        "Reason" : "Cyberduel",
        "Years" : [1991, 1992, 1993]
    },
    2: {
        "name" : "Mace",
        "surname" : "Windu",
        "Death" : "Coruscant",
        "Reason" : "Cyberduel",
        "Years" : [1995, 1996, 1998]
    }
}

result = councilJedi[1]["Years"][0]
print(result)
