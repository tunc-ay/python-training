names = ["Luke", "Leia", "Obiwan", "Yoda", "Anakin"]
years = [1998, 2000, 1998, 1987]

# Q1 > Add Mace Windu to the list to the last
names.append("Mace Windu")

# Q2 > Add "Plo Koon" to the beginning of the list
names.insert(0, "Plo Koon")

# Q3 > Remove the last member from the list
names.pop(-1)

# Q4 > The index of Obiwan
x = names.index("Obiwan")

# Q5 > whether Anakin is a member of the list
x = names.index("Anakin")
x = "Anakin" in names

# Q6 > reverse the list
names.reverse()

# Q7 > alphabetical order
names.sort()

# Q8 > sort years
years.sort()

# Q9 > change the following into a list
phones = "iPhoneX, iPhoneXR"
phones = phones.split()

# Q10 > max and min of Years
result = max(years)
result1 = min(years)

# Q11 > how many 1998 in years
print(years.count(1998))


print(phones)
print(years)
print(names)
print(result)
print(result1)
print(x)