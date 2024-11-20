def count_divisible_by_3(L, R):
    first = L if L % 3 == 0 else L + (3 - L % 3)
    last = R if R % 3 == 0 else R - (R % 3)
    if first > R:
        return 0
    return (last - first) // 3 + 1

l, r = map(int, input().split())
print(count_divisible_by_3(l, r))