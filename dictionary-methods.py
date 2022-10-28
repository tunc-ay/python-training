jediMaster = {
    "name" : "Obiwan Kenobi",
    "planet": "Tatooine",
    "death":"Death Star"
}

# result = jediMaster.get("name")

# for x in jediMaster.values():
#     print(x)

# for x,y in jediMaster.items():
#     print(x,y)

# print(result)

# jediMaster["Enemy"]="Sith"

# jediMaster.pop("death")

# del jediMaster["death"]

jediCouncil = jediMaster.copy()
jediCouncil["name"] = "Yoda"

print(jediMaster)
print(jediCouncil)