# Try - except block not to blow the code.
#example1
try1 = "Hello bob"
try: 
    try2 = int(try1)
except:
    try2 = 789
print("First", try2)

try3 = 345
try: 
    try2 = int(try3)
except:
    try2 = -1
print("Second", try2)

#example2
rawNo = input("Enter a number: ")
try:
    rawNo1 = int(rawNo)
except: 
    rawNo1 = -1
if rawNo1 > 0 :
    print("Nice work")
else:
    print("Please, enter a proper number")

