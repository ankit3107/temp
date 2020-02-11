def reverseArray(a):
    len_a = len(a)
    reverse_list = []
    while len_a > 0:
        len_a -= 1
        print(a[len_a])
        reverse_list.append(a[len_a])

    return reverse_list


reverseArray([1, 2, 3])

