from collections import defaultdict

cnt = 0
o = defaultdict(set)
for s in open("input.txt").read().split():
    if "|" in s:
        l, r = map(int, s.split("|"))
        o[l].add(r)
    else:
        p = list(map(int, s.split(",")))
        cnt += p[len(p)//2]*all(not o[x] & set(p[:i]) for i, x in enumerate(p))
print(cnt)
