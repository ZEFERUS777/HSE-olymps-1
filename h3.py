n = int(input())
a = list(map(int, input().split()))

call_n = set(a)

first_m = 0
secnd_m = 0
count = 0

for i in range(1, 2 * n + 2):
    if i not in call_n:
        count += 1
        if count == 1:
            first_m = i
        elif count == 2:
            secnd_m = i
            break

print(secnd_m)