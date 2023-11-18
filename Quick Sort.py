def quick_sort(newlist):
    quick_sort2(newlist, 0, len(newlist)-1)
    return newlist

def quick_sort2(newlist, low, hi):
    if low < hi:
        p = partition(newlist, low, hi)
        quick_sort2(newlist, low, p-1)
        quick_sort2(newlist, p+1, hi)

def get_pivot(newlist, low, hi):
    mid = (hi+low)//2
    pivot = hi
    if newlist[low] < newlist[mid]:
        if newlist[mid] < newlist[hi]:
            pivot = mid
    elif newlist[low] < newlist[hi]:
        pivot = low
    return pivot

def partition(newlist, low, hi):
    pivotIndex = get_pivot(newlist, low, hi)
    pivotValue = newlist[pivotIndex]
    newlist[pivotIndex], newlist[low] = newlist[low], newlist[pivotIndex]
    border = low

    for i in range(low, hi+1):
        if newlist[i] < pivotValue:
            border += 1
            newlist[i], newlist[border] = newlist[border], newlist[i]
    newlist[low], newlist[border] = newlist[border], newlist[low]

    return (border)



user_list = input("Enter numbers separated by a comma:")
user_list = [int(i) for i in user_list.split(",")]
print(f"Before sorting {user_list}")
print(f"After sorting {quick_sort(user_list)}")