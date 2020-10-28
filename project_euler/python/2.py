def fib(n):

    """ Returns the nth element of the fibonnaci sequence.

    Args
    ---
    n: index of fibonnaci sequence

    Returns
    ---
    result: nth element of the fibonnaci sequence

    """

    # Base case
    if n <= 1:
        result = 1
        return result

    result = fib(n-1) + fib(n-2)

    return result


def sum_even_valued_terms(upper_limit):
    """ Finds the sum of even valued elements of the fibonnaci
    sequence which are individually less than upper_limit

    Args
    ---
    upper_limit: Number that the nth term of the fibonnaci sequence
    should be less than

    Returns
    ---

    sum(even_list): Sum of even valued elements < upper_limit
    """

    value_list = []
    n = 0
    while fib(n) < upper_limit:
        value_list.append(fib(n))
        n += 1

    sum_even_list = sum([x for x in value_list if (x % 2 == 0)])

    return sum_even_list



sum_fib = sum_even_valued_terms(4e6)
print(f"The sum is {sum_fib}")
