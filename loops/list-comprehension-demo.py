# Q1 > print numbers between 1 and 100 that can be divided by 12 
numbers = [i for i in range(1, 101) if i%3==0 and i%4==0]
print(numbers)

# Q2 > turn names into lower case and write them from the end to beginning
names = ["Jonny", "RiCk", "DaVid", "ShweTal"]
result= [i.lower()[::-1] for i in names]
print(result)

# Q3 > pick only numbers to create a list
string = "Hello 12345 World"
stringNum = [i for i in string if i.isdigit()]
print(stringNum)

# Q4 > print ages based on the year
import datetime
today = datetime.date.today().year
years = [1983, 1999, 2008, 1956, 1986, 1981]
result = [today-i for i in years]
print(result)

# Q5 > print warning message for minus santigrat degrees
degrees = [20, 5, 15, -2, 0, -6]
degreeMinus = [i if i > 0 else "Danger" for i in degrees]
print(degreeMinus)