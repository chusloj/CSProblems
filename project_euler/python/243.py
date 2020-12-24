threshold = 15499/94744

def find_Rd(denom):
    if denom<10:
        raise ValueError

    basic_list = []
    for i in range(2, 10):
        if denom % i == 0:
            basic_list.append(i)

    if len(basic_list) == 0:
        return 9e99999

    non_basic_list = []
    for num in range(max(basic_list)+1, denom):
        for i in basic_list:
            if (num % i == 0) and (num not in non_basic_list):
                non_basic_list.append(num)


    R = (denom-1) - (len(basic_list) + len(non_basic_list))
    ratio = R / (denom-1)

    return ratio


def find_smallest_denom(start_denom, threshold):
    denom = start_denom
    while find_Rd(denom) >= threshold:
        denom += 1
    return denom

print(find_smallest_denom(15, threshold))
