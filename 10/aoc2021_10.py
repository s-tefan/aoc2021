
def partonetwo(input):
    scorelist, score2list = [], []
    for line in input:
        linescore, openings = parse([], iter(line))
        scorelist.append(linescore)
        if not linescore:
            s = 0
            while openings:
                s *= 5
                s += score2[openings.pop()]
            score2list.append(s)
    return sum(scorelist), sorted(score2list)[len(score2list)//2]

pairs = {'<': '>', '[': ']', '(': ')', '{': '}'}
score = {')': 3, ']': 57, '}': 1197, '>': 25137}
score2 = {'(': 1, '[': 2, '{': 3, '<': 4}
def parse(cs, iterline):
    n = next(iterline)
    if n in pairs:
        cs.append(n)
        return parse(cs, iterline)
    elif n in pairs.values():
        if pairs[cs[-1]] == n:
            return parse(cs[:-1], iterline)
        else:
            return score[n], cs
    else:
        return 0, cs

with open("input.txt") as f:
    input = f.readlines()
    print(partonetwo(input))
