from unittest import result

website = "http://www.sadikturan.com"
courseName = "Python Dersleri: Sifirdan ileri seviye Python programlama"

#Q1: ' Hello World ' delete emptiness before and after 
sentence = " Hello World ".strip()

#Q2: delete the website except sadikturan 
print(website.strip("htp./com:w"))

#Q3: lowercase the course name
print(courseName.lower())

#Q4: how many 'a' within the website
print(website.count("a"))

#Q5: does the website starts with "www" and ends with "com"
print(website.startswith("www"))
print(website.endswith(".com"))

#Q6: is there ".com" within the website
sentenceList = website.split(".")
sentenceList1 = website.find(".com")
print(sentenceList.index("com"))
print(sentenceList1)



#Q7: is the courseName alphabetic?
print(courseName.isalpha())

#Q8: place "contents" in 50 chars and place * before and after
msg = "Contents"
msg1 = "*" * 20  
print(msg1 + "*" + msg + "*" + msg1)


#Q9: change all blank in the courseName with "-"
sentenceNew = courseName.split()
sentenceNew = "-".join(sentenceNew)
print(sentenceNew)

#Q10: change world with there in  "Hello World"
helloWorld = "Hello World"
print(helloWorld.replace("World", "there"))

#Q11: change all blanks in courseName with "-"
sentenceNew = courseName.split()
print(sentenceNew)
