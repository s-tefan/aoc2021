def partone(input):
    stripped_input = [k.strip() for k in input]
    n = len(input)
    tr = zip(*stripped_input)
    ones = list(map(lambda x : x.count('1'), tr))
    delta, epsilon = 0, 0
    for k in ones:
        delta <<= 1
        epsilon <<= 1
        if k >= n-k:
            delta |= 1
        else:
            epsilon |= 1
    return epsilon*delta

def brupp(codelist, bitpos, mc = True):
    other = lambda x : '0' if x == '1' else '1'
    n = len(codelist)
    ones = [x[bitpos] for x in codelist].count('1')
    most_common = '1' if ones >= n - ones else '0'
    return list(filter(lambda x : x[bitpos] == (most_common if mc else other(most_common)), codelist) )


def parttwo(input):
    stripped_input = [k.strip() for k in input]
    oxygen = stripped_input
    co2scrub = stripped_input
    bitpos = 0
    while len(oxygen) > 1:
        oxygen = brupp(oxygen, bitpos, True)
        bitpos += 1
    bitpos = 0
    while len(co2scrub) > 1:
        co2scrub = brupp(co2scrub, bitpos, False)
        bitpos += 1
    return int(oxygen[0],2)*int(co2scrub[0],2)

with open("input.txt") as f:
    input = f.readlines()
    print(partone(input))
    print(parttwo(input))
