def diff():
    sum_of_squares = sum([x**2 for x in range(1,101)])
    square_of_sum = ((100*101)/2)**2

    return abs(sum_of_squares - square_of_sum)

print(diff())