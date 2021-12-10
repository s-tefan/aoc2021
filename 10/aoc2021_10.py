
def partone(input):
    scorelist = []
    for line in input:
        linescore = parse(iter(line))
        scorelist.append(linescore)
        print()
    return scorelist

pairs = {'<': '>', '[': ']', '(': ')', '{': '}'}
score = {')': 3, ']': 57, '}': 1197, '>': 25137}

# Det blr inte rätt
def getchunk(iterline, c):
    n = next(iterline)
    if n in pairs:
        print(c, end='')
        return getchunk(iterline, c) # Här får kollas
    elif n in pairs.values():
        if n == pairs[c]:
            print(n, end='')
            return 0
        else:
            print(n, end='!')
            return score[n]
    else:
        return 0



def parse(iterline):
    c = next(iterline)
    while True:
        getchunk(iterline, c)



with open("test.txt") as f:
    input = f.readlines()
    print(partone(input))
