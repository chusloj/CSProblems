def check(n, factors):
    for f in factors: # testing reveals that starting from lowest factor first is fastest
        if n % f != 0: # lesson: "Don't waste time"
            return False
    return True



def smallest_multiple(start_n):
    n = start_n
    factors = [x for x in range(11,20+1)]
    while check(n, factors) == False:
        n += 1

    return(n)

# Driver
print(smallest_multiple(20))