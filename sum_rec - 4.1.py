def sum_rec(arr: list) -> int:
    if not arr:
        return 0
    else:
        return arr[0] + sum_rec(arr[1:])

print(sum_rec([2, 4, 6]))  # 12