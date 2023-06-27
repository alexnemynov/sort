def max_num_rec(arr: list) -> int:
    if len(arr) == 1:
        return arr[0]
    else:
        a, b = arr[0], max_num_rec(arr[1:])
        # print(a, b)
        return a if a > b else b

print(max_num_rec([2, 4, 6, 0, 1, 9, 8, 10, 7, 9]))  # 10