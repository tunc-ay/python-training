#Student information
from datetime import date, datetime
from math import prod

studentName = "Oktay"
studentSurname = "Kayaoglu"
studentFullName = studentName + '' + studentSurname
studentNo = "356"
studentGender = "M"
studentCitizenNo = "123456789"
studentBirthday = 2014
studentAddress = "Istanbul"
studentAge = 2022 - studentBirthday

prod1 = 50
prod2 = 60.5
prod3 = 356.45 
total = prod1 + prod2 + prod3
print(total)