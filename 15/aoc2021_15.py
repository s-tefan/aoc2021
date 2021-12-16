from math import inf

def main():
    with open("input.txt") as f:
        cave = [[int(x) for x in row.strip()] for row in f.readlines()]
        print(partone(cave))
        print(parttwo(cave))


def value(cave, node):
    return cave[node[0]][node[1]]

def neighbour_set(node, m, n):
    nset = set()
    if node[0] > 0: nset.add((node[0]-1, node[1]))
    if node[0] < m-1: nset.add((node[0]+1, node[1]))
    if node[1] > 0: nset.add((node[0], node[1]-1))
    if node[1] < n-1: nset.add((node[0], node[1]+1))
    return nset

def minimal_risk(risk, aset):
    acave = {x: risk[x] for x in aset}
    #print(acave)
    return min(acave, key=acave.get)

def partone(cave):
    m, n = len(cave), len(cave[0])
    last_node = (m-1, n-1)
    unvisited_set = {(i,j)
        for i in range(m)
        for j in range(n)}
    risk = {node: inf for node in unvisited_set}
    risk[(0,0)] = 0
    current_node = (0,0)
    while last_node in unvisited_set:
        #print(current_node, risk[current_node], unvisited_set)
        for unvisited_neighbour in \
            neighbour_set(current_node, m, n) & unvisited_set:
                tentative_risk = risk[current_node] + \
                    value(cave, unvisited_neighbour)
                if tentative_risk < risk[unvisited_neighbour]:
                    risk[unvisited_neighbour] = tentative_risk
        unvisited_set.remove(current_node)
        if unvisited_set:
            current_node = minimal_risk(risk, unvisited_set)
    #print("***", risk)
    return risk[last_node]

def rollover(x):
    if x > 9:
        return x - 9
    else:
        return x

def parttwo(cave):
    bigcave = []
    for k in range(5):
        for row in cave:
            bigcave.append([rollover(x+k) for x in row])
    for row in bigcave:
        brow = list(row)
        for k in range(1,5):
            row += [rollover(x+k) for x in brow]
    return partone(bigcave)

main()
