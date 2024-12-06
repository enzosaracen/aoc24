from collections import defaultdict

cnt = 0
o = defaultdict(set)
for s in open("input.txt").read().split():
    if "|" in s:
        l, r = map(int, s.split("|"))
        o[l].add(r)
    else:
        p = list(map(int, s.split(",")))
        if any(o[x] & set(p[:i]) for i, x, in enumerate(p)):
            cnt += [x for x in p if len(set(p) & o[x]) == len(p)//2][0]
print(cnt)
