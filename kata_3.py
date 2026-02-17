def descending_order(num):
    num_list = list(str(num))
    num_list.sort()
    num_list.reverse()
    return int("".join(num_list))

descending_order("12438")
