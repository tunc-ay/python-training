from re import T


isLoggedin = True
if isLoggedin == True:
    print("Welcome")

if isLoggedin: print("Welcome!")

###
username = "obiwan-kenobi"
password = "1234"

isLoggedin = (username == "obiwan-kenob") and (password == "1234")
if isLoggedin: 
    print("May be force be with you!")
else: 
    print("Your information are not correct")