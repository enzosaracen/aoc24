g = [list("."+l.strip()+".") for l in open("input.txt").readlines()]
n, m = len(g)+2,len(g[0])
g = [["."]*m]+g+[["."]*m]

cnt = 0
for i in range(1,n-1):
    for j in range(1,m-1):
        if g[i][j] == "A":
            cnt += all([g[i-1][j+k]+g[i+1][j-k] in "MSM" for k in (-1,1)])
print(cnt)
