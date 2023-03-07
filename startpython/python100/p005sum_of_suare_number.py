def sum_of_square(n):
    SUM = 0
    for number in range(1, n+1):
        SUM += number*number
    return SUM

print("sum of square3:", sum_of_square(3))
