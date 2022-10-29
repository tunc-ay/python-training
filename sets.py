# A set is a collection which is unordered, unchangeable, and unindexed.

jediMasters = {"Obiwan Kenobi", "Yoda", "Mace Windu"}
sith = {"Anakin", "Palpatine"}

jediMasters.add("Luke")
jediMasters.update(["Luke", "Leia"])
jediMasters.remove("Mace Windu")        # removes an item
jediLen = len(jediMasters)
jediFind = "Anakin" in jediMasters

result = jediMasters.union(sith)

# print(jediMasters[0])       # this does not work

print(jediMasters)            # this lists different ordered sets everytime.
print(jediLen)
print(jediFind)
print(result)

