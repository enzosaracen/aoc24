from collections import defaultdict

l = []
r = defaultdict(int)
for n in open("input.txt").readlines():
    n = list(map(int, n.split()))
    l.append(n[0])
    r[n[1]] += 1
print(sum(i*r[i] for i in l))
