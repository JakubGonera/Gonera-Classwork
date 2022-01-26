# Binary Search Animals
nameList = ["baboon","cheetah","elephant","giraffe","hippo","leopard","lion","mongoose","rhino","warthog"]

def binSearch(l, r, item):
    if(r < l):
        print("animal not found in the list")
        return
    #end if
    m = (l + r) // 2
    print (l, " ", r, " ", m, " ", nameList[m])
    if nameList[m] == item:
        print("animal found at index ", m)
    elif item < nameList[m]:
        binSearch(l, m - 1, item)
    else:
        binSearch(m + 1, r, item)
    #end if
#end procedure

animal = "lion"

binSearch(0, len(nameList) - 1, animal)

input("\nPress ENTER to exit program ")