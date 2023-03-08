#Tyfabian Williams
#2142655

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

solution = False

for x in range(-10, 10):
    for y in range(-10, 10):
        if ((a * x + b * y) == c) and ((d * x + e * y) == f):
            solution = True
            print(x, y)
if not solution:
    print('No solution')
