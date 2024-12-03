import re
from math import prod

print(sum(prod(map(int, m)) for m in re.findall(r"mul\((\d+),(\d+)\)", open("input.txt").read())))
