mobilePhone = ["Samsung S5", "Samsung S6", "Samsung S7", "Samsung S8"]

#Q1 > how many char are there in the mobilePhone
print(len(mobilePhone))

#Q2 > first and last element
print(mobilePhone[0], mobilePhone[-1])

#Q3 > change Samsung S5 with Samsung S9
mobilePhone[0] = "Samsung S9"
print(mobilePhone)

#Q4> Samsung S6 is an item within the list?
if "Samsung S6" in mobilePhone:
    print("evet")

#Q5 > -3 element of the list?
print(mobilePhone[-3])

#Q6 > first two elements of the list
print(mobilePhone[0:2])

#Q7 > change the last two elements with Samsung S9 and Samsung S10
mobilePhone[-1] = "Samsung S9"
mobilePhone[-2] = "Samsung S10"
print(mobilePhone)

#Q8 > Add iPhoneX and iPhoneXR
mobilePhone2 = mobilePhone + ["iPhoneX", "iPhoneXR"]
print(mobilePhone2)

#Q9 > delete the last element
del mobilePhone2[-1]
print(mobilePhone2)

#Q10 > reverse the list's element
print(mobilePhone2[::-1])

#Q11 >

userA = ["Obiwan Kenobi", 2010, [70,60,70]]
userB = ["Luke Skywalker", 1999, [80,90,80]]
userC = ["Leia Organa", 1999, [80,60,70]]
print(userA,userB,userC)


