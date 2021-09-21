print("Input the width of the room:")

w = int(input())

print("Input the depth of the room:")

d = int(input())

print("Input the height of the room:")

h = int(input())

print("Input number of layers:")
l = int(input())

print("Input the amount of unpaintable areas:")
n = int(input())

area = w * h * 2 + d * h * 2

for i in range(0, n):
    print("Input two dimensions of the area:")
    x = int(input())
    y = int(input())
    area -= x * y

area *= l
out = area/11
print("You need",out, "litres of paint")