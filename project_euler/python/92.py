# chains ALWAYS end at 1 or 89 – use that

def next_chain(num):
    return sum(int(digit)**2 for digit in str(num))

def find_termination(start_num):
    num = start_num
    while (num != 1) and (num != 89): # this was the problem
        num = next_chain(num)
    return num


def find_arriving_nums():
    count_89 = 0
    for num in range(1,10000000):
        if find_termination(num) == 89:
            count_89 += 1
    return count_89



print(find_arriving_nums())
