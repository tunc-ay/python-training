from itertools import count


n = 5
while n > 0:
    print("i love you")
    n = n - 1
print("Yuppiieee")


while True:
    line = input('>')
    if line == 'done':
        print("done")
        break                   # if no 'break', it is infinite loop.
print("Don't")


while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)                  
print("Don't")


n = -1
print("Before", n)
for num in [9, 4, 21, 90, 98, 3]:
    if num > n:
        n = num
    print(n, num)
print("After", n)


count = 0
sum = 0
print("Before", count, sum)
for value in [9,0, 111, 222]:
    count = count + 1
    sum = sum + value
    print(count, sum, value) 
print("After", count, sum, value)
