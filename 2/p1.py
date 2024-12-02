def safe(l):
    o = 1 if l[0] < l[-1] else 0
    p = l[0]
    for i in l[1:]:
        d = abs(p-i)
        if d < 1 or d > 3 or (i < p) == o:
            return 0
        p = i
    return 1

cnt = 0
for n in open("input.txt").readlines():
    cnt += safe(list(map(int, n.split())))
print(cnt)
