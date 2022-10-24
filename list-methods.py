numbers = [1, 5, 8, 9, 45, 74]
letters = ["a", "b", "c", "a", "d", "e"]

result = min(numbers)   # minimum number
result = max(numbers)   # maximum number 
result = min(letters)   

numbers.append(10)      # add a number to a list
numbers.insert(3, 100)  # add a number to designated position. In this case, it is "3"
numbers.insert(len(numbers), 1599) # add 1599 at the end.

numbers.pop()     # deletes the number at the end.
numbers.pop(1)     # deletes the designated place.
numbers.remove(9)   #removes the number 9

numbers.sort()      # sort the numbers.
numbers.reverse()   # reverse the sort.

print(numbers.count(74))
print(numbers.index(8))

print(numbers.clear())

print(numbers)
