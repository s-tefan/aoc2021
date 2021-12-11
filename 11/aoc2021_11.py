from copy import deepcopy

def inc_all(a):
     for row in a:
         for k, c in enumerate(row):
             row[k] += 1

def flash(a):
    return {(k,m) for (k,r) in enumerate(a) for (m,c) in enumerate(r) if r[m] > 9}

def neighbours(i, j, m, n):
    return {(a, b) for a in range(i-1, i+2) for b in range(j-1, j+2) if
        (a,b) != (i,j) and a in range(m) and b in range(n)}

def set_zero(a, pos_set):
    for (i,j) in pos_set:
        a[i][j] = 0

def flash_neighbours(array, pos_set):
    for (i,j) in pos_set:
        for (a,b) in neighbours(i,j,m,n):
            if array[a][b] != 0:
                array[a][b] += 1

def pprint(array):
    for row in array:
        print(''.join(str(x) for x in row))
    print()


def partone(octopus_energy):
    no_flashes = 0
    for k in range(100):
        flashes_this_step = 0
        inc_all(octopus_energy)
        while True:
            flashed = flash(octopus_energy)
            flashes_this_step += len(flashed)
            set_zero(octopus_energy, flashed)
            flash_neighbours(octopus_energy, flashed)
            if not flashed:
                break
        no_flashes += flashes_this_step
    return no_flashes

def parttwo(octopus_energy):
    steps = 0
    while True:
        steps += 1
        inc_all(octopus_energy)
        no_flashes_this_step = 0
        while True:
            flashed = flash(octopus_energy)
            no_flashes_this_step += len(flashed)
            if no_flashes_this_step == n*m:
                return steps
            set_zero(octopus_energy, flashed)
            flash_neighbours(octopus_energy, flashed)
            if not flashed:
                break

with open("input.txt") as f:
    octopus_energy = []
    for line in f.readlines():
        octopus_energy.append([int(x) for x in line.strip()])
m = len(octopus_energy)
n = len(octopus_energy[0])
print(partone(deepcopy(octopus_energy)))
print(parttwo(deepcopy(octopus_energy)))
