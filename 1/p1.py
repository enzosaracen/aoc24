l = []
r = []
for n in open("input.txt").readlines():
    n = list(map(int, n.split()))
    l.append(n[0])
    r.append(n[1])
l.sort()
r.sort()
print(sum(abs(i-j) for i, j in zip(l, r)))
