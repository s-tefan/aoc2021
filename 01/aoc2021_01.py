# aoc2021_01.py

def a(depths):
    sinks = [(depths[n+1]-depths[n]) > 0 for n in range(len(depths)-1)]
    return sinks.count(True)
def b(depths):
    sinks = [(depths[n+3]-depths[n]) > 0 for n in range(len(depths)-3)]
    return sinks.count(True)

with open("input.txt") as f:
    input = f.readlines()


depthlist = [int(x) for x in input]
print(a(depthlist))
print(b(depthlist))


