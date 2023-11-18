def insertion_sort(values):
    for i in range(1, len(values)):
        j = i-1
        while values[j] > values[j+1] and j >= 0:
            values[j], values[j+1] = values[j+1], values[j]
            j -= 1
    return values

user_list = input("Enter numbers separated by a comma:")
user_list = [int(i) for i in user_list.split(",")]
print(f"Before sorting {user_list}")
print(f"After sorting {insertion_sort(user_list)}")


    