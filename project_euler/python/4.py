def largest_palindrome_product():

    n = 0
    for a in range(999, 100, -1): #search all 3 digit numbers
        for b in range(a, 100, -1):
            x = a * b
            if x > n:
                s = str(a * b)
                if s == s[::-1]: # if forward equals backward
                    n = a * b
    return n

largest_palindrome_product()
