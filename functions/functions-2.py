def now():
    import datetime
    return datetime.datetime.now().hour

def greetings():
    if (now() < 12):
        return "Good Morning"
    elif (now() > 12 or now() < 17):
        return "Have a nice day"
    else: return "Good evening"
print(greetings())

###
def year():
    import datetime
    return datetime.datetime.now().year

def licenseCalc(myAge, name):
    age = year() - myAge

    if age > 18:
        print(f"{name} can get a driving license")
    else: print(f"{name} cannot get a driving license")

x = licenseCalc(1967, "Obiwan")
