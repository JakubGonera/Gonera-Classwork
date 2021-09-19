def is_in_list(l, c):
    for x in l:
        if c == x:
            return True
        #end if
    #next

    return False
#end function

def gen_perm(list_of_chars, n):
    if n == 1:
        for c in list_of_chars:
            yield [c]
        #next
    #end if
    else:
        last_list = gen_perm(list_of_chars, n - 1)
        for l in last_list:
            for c in list_of_chars:
                if is_in_list(l, c) == False:
                    yield ([c] + l)
                #end if
            #next
        #next
    #end else
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