
def solve():
    n = int(input())
    current = list(map(int, input().split()))
    target = list(map(int, input().split()))
    neg_val_count = 0
    diff_arr = []
    for i in range(n):
        diff = current[i] - target[i]
        diff_arr.append(diff)
        if diff < 0:
            neg_val_count += 1
    if neg_val_count >= 2:
        return print("NO")
    elif neg_val_count == 0:
        return print("YES")
    else:
        for i in range(n):
            if diff_arr[i] < 0:
                for j in range(n):
                    if diff_arr[j]>= diff_arr[i]:
                        return print("YES")
                return print("NO")

res = []
for i in range(int(input())):
    res.append(solve())
for i in res:
    if i != None:
        print(i)

