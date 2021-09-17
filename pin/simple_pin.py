def is_in_list(l, c):
    for x in l:
        if c == x:
            return True
        #end if
    #next

    return False
#end function

def gen_perm(list_of_chars, n):
    out = []
    if n == 1:
        for c in list_of_chars:
            out.append([c])
        #next
        return out
    #end if
    last_list = gen_perm(list_of_chars, n - 1)
    for c in list_of_chars:
        for l in last_list:
            if is_in_list(l, c) == False:
                out.append([c] + l)
            #end if
        #next
    #next
    return out
#end function


print('Input the number of digits: ')

n = int(input())

print('Input the digits: ')

l = []

for x in range(0, n):
    l.append(int(input()))
#next

perm = gen_perm(l, n)

for x in perm:
    for y in x:
        print(y, end='')
    #next
    print('\n')
#next