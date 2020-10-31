def find_max(num):

    digits = get_digits(num)
    length = len(digits)

    max = (9**5) * length
    return max


def get_digits(num):

    s = str(num)
    l = list(s)
    digits = [int(x) for x in l]

    return digits




def fifth_power_sum():

    nums = []
    for i in range(10000,100000):
        if i == sum_fifth_power_digits(i):
            nums.append(i)

    return sum(nums)





# answer
l = [i for i in range(10, 354294) if i == sum(int(d) ** 5 for d in str(i))]
s = sum(l)
s
