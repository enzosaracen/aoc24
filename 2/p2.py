def safe(l, bad=0):
    o = 1 if l[0] < l[-1] else 0
    p = l[0]
    for i, v in enumerate(l[1:]):
        d = abs(p-v)
        if d < 1 or d > 3 or (v < p) == o:
            if bad:
                return 0
            else:
                return safe(l[:i]+l[i+1:], 1) or safe(l[:i+1]+l[i+2:], 1)
        p = v
    return 1

cnt = 0
for n in open("input.txt").readlines():
    cnt += safe(list(map(int, n.split())))
print(cnt)
