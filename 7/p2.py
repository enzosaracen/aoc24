def eqn(r, c, x):
    if not x: return r if r == c else 0
    return max(eqn(r, c+x[0], x[1:]), eqn(r, c*x[0], x[1:]), eqn(r, int(str(c)+str(x[0])), x[1:]))

ans = 0
for l in open("input.txt").readlines():
    r, x = l.split(":")
    x = list(map(int, x.split()))
    ans += eqn(int(r), x[0], x[1:])
print(ans)
