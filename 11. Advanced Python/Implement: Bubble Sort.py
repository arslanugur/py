# Bubble Sort is used to sort a list of elements, by comparing two adjacent elements and swapping them, if they are not in order.
def bubble_sort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for j in range(passnum):
            if nlist[j]>nlist[j+1]:
                nlist[j], nlist[j+1] = nlist[j+1], nlist[j]

nlist = [14,46,43,27,57,41,45,21,70]
bubble_sort(nlist)
print(nlist)

# output: [14, 21, 27, 41, 43, 45, 46, 57, 70]

# Bubble Sort is used to sort a list of elements, by comparing two adjacent elements and swapping them, if they are not in order


# Easier example:
def bubble_sort(list):
    for i in range(0, len(list) - 1):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list




# Bubble Sort
myList = [8,4,1,3,2,6]
count = 0
for i in range(len(myList)-1):
 for t in range(len(myList)-1):
         if myList[t]>myList[t+1]:
             myList[t],myList[t+1] = myList[t+1],myList[t]
             count += 1
print(myList,count)


