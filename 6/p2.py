g = [list(l.strip()) for l in open("input.txt").readlines()]
n = len(g)

def sim():
    rot = 0
    dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    dx, dy = dir[rot]
    y, x = next((i, j) for i in range(n) for j in range(n) if g[i][j] == "^")
    s = [[set() for _ in range(n)] for _ in range(n)]
    while 0 <= x < n and 0 <= y < n:
        if rot in s[y][x]:
            return 1
        s[y][x].add(rot)
        while 0 <= x+dx < n and 0 <= y+dy < n and g[y+dy][x+dx] == "#":
            rot = (rot + 1) % 4
            dx, dy = dir[rot]
        x += dx
        y += dy
    return 0

cnt = 0
for i in range(n):
    for j in range(n):
        if g[i][j] == ".":
            g[i][j] = "#"
            cnt += sim()
            g[i][j] = "."
print(cnt)
