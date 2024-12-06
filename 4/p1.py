adj8 = [(dx,dy) for dx in (-1,0,1) for dy in (-1,0,1) if (dx,dy) != (0,0)]

g = [list("..."+l.strip()+"...") for l in open("input.txt").readlines()]
n, m = len(g)+6,len(g[0])
g = [["."]*m]*3+g+[["."]*m]*3 

cnt = 0
for i in range(3,n-3):
    for j in range(3,m-3):
        for dx,dy in adj8:
            cnt += list("XMAS") == [g[i+dx*k][j+dy*k] for k in range(4)]
print(cnt)
