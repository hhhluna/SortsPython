def bubble_sort(values):
    for i in range(0, len(values)-1):
        for j in range (0, len(values)-1-i):
            if values[j] > values[j+1]:
                values[j], values[j+1] = values[j+1], values[j]
    return values












user_list = input("Enter numbers separated by a comma:")
user_list = [int(i) for i in user_list.split(",")]
print(f"Before sorting {user_list}")
print(f"After sorting {bubble_sort(user_list)}")


