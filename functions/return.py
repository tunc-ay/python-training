def adding():
    return f'adding: {10+20}'

a = adding()
print(a)
print(adding())


# two functions to calculate age
def now():
    import datetime
    return datetime.datetime.now().year

def myAge():
    return now()-1981

print(myAge())