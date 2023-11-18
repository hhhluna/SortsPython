def linear_sort_func(values):
    num_sort = [] 
    i = 0 
    a = 1  

    while values:  
        if values[i] == values[-1] and values[i] <= a:  
            num_sort.append(values.pop(i))
            i = 0
        elif values[i] == values[-1]:  
            i = 0  
            a += 1  
        elif values[i] <= a:  
            num_sort.append(values.pop(i))
            i = 0  
            a += 1  
        else:  
            i += 1  
    return num_sort



user_list = input("Enter numbers separated by a comma:")
user_list = [int(i) for i in user_list.split(",")]
print(f"Before sorting {user_list}")
print(f"After sorting {linear_sort_func(user_list)}")
