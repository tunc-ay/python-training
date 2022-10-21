lang = ["JavaScript", "Java", "Python", "C#"]

lang[1] = "HTML" #changing the first element of the list

lang2 = lang + ["VueJS", "Angular"] # the lang list does not change; we created a new list. 

print(lang[0:2]) #zero, first element of the list
print(lang[2:]) #second and elements after the second
print(lang2)

if "HTML" in lang:
    print("Yes!")

del lang[2] #to delete certain item within the list.
print(lang)

