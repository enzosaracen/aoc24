import re
from math import prod

s = open("input.txt").read()
good = ""
start = 0
while True:
    i = s.find("don't()", start)
    if i == -1:
        good += s[start:]
        break
    good += s[start:i]
    i = s.find("do()", i)
    if i == -1:
        break
    start = i

print(sum(prod(map(int, m)) for m in re.findall(r"mul\((\d+),(\d+)\)", good)))
