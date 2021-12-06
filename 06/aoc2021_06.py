def ver_one(input, gens):
    state = [int(x) for x in input.strip().split(',')]
    newborn = 0
    for gen in range(gens):
        for k, n in enumerate(state):
            match n:
                case 0:
                    newborn += 1
                    state[k] = 6
                case _:
                    state[k] -= 1
        state += [8]*newborn
        newborn = 0
        #print(state)
    return len(state)

def ver_two(input, gens):
    fish_timers_init = [int(x) for x in input.strip().split(',')]
    n = 8
    nos = [0]*(n+1)
    for k in fish_timers_init:
        nos[k] += 1
    newborn = 0
    for gen in range(gens):
        mothers = nos[0]
        for k in range(n):
            nos[k] = nos[k+1]
        nos[n] = mothers
        nos[6] += mothers
        newborn = 0
    return sum(nos)

with open("input.txt") as f:
    input = f.readline()
    print(ver_two(input, 80))
    print(ver_two(input, 256))
