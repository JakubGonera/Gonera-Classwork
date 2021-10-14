max = 'a'
min = 'z'

for i in range(0, 5):
    print('Input letter')
    c = input()
    if c < min:
        min = c
    if c > max:
        max = c
print("The largest letter was:", max)
print("The smallest letter was:", min)
