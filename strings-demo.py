from tkinter import W


website = "http://www.sadikturan.com"
courseName = "Python Dersleri: Sifirdan ileri seviye Python programlama"

# Q1: number of chars in 'courseName'
numberOfChar = len(courseName)
print(numberOfChar) # 57

# Q2: 'www' out of website
print(website[7:10]) 

# Q3: 'com' out of website
print(website[-3:])

# Q4: first and last 15 chars in 'courseName'
print(courseName[0:15]) 
print(courseName[-15:])

# Q5: reverse 'courseName'
print(courseName[::-1])

# Q6: change w with W in 'Hello world'
hello = "Hello world"
hello2 = hello[0:5] + ' ' + 'W' + hello [7:11]
print(hello.title())
print(hello2)

# Q6: repeat abc three times
repeat = "abc" * 3
print(repeat)

myName = "Bora"
mySurname = "Yılmaz"
myAge = "32"
myOccupation = "engineer"
print(f"My name is {myName} {mySurname}. I am {myAge} years-old. My occupation is {myOccupation}.")
