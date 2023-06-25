def count_list_rec(arr: list) -> int:
    if not arr:
        return 0
    else:
        return 1 + count_list_rec(arr[1:])

print(count_list_rec([2, 4, 6]))  # 3