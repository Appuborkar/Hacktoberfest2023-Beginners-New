'''Without using temp variable'''
def bubble_sort(list):
    for i in range(0,len(list)-1):
        for j in range(len(list)-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    return list
list=[8,3,4,2,5,6,1,0]
print("The list of unsorted list is ",list)
print("The list of sorted list is",bubble_sort(list))
