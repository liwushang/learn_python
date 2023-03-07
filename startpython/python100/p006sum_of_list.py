def sum_list(param_list):
    total = 0
    for i in param_list:
        total += i
    return total

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"sum of list:{sum_list(list)}")
print(sum(list))
