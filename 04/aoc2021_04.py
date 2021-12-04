class Bricka:

    def __init__(self, rows = []):
        self.rows = rows

    def check_bingo(self, drawn):
        rowbingo = any(map(lambda row: all( map (lambda number: number in drawn, row)), self.rows))
        if rowbingo:
            return True
        colbingo = any(map(lambda row: all( map (lambda number: number in drawn, row)), zip(*(self.rows))))
        if colbingo:
            return True
        return False

    def sum_of_unmarked(self, drawn):
        unmarked = filter(lambda x: not(x in drawn), [k for row in self.rows for k in row])
        return(sum(unmarked))

def partboth(input):
    lines = iter(input)
    numbers = [int(x) for x in next(lines).strip().split(',')]
    brickor = set()
    bricka = Bricka()
    brickrows = []
    for line in lines:
        if line.strip():
            brickrows.append([int(x) for x in (line.strip().split())])
        else: # blank line
            if brickrows:
                brickor.add(Bricka(rows=brickrows))
                brickrows = []
    no_win = True
    if brickrows:
        brickor.add(Bricka(rows=brickrows))
    for k in range(len(numbers)):
        nums = numbers[0:k]
        to_remove = set()
        for bricka in brickor:
            if bricka.check_bingo(nums):
                latest = {'rounds': k, 'last drawn': nums[-1], 'sum of unmarked': bricka.sum_of_unmarked(nums), 'score': nums[-1]*bricka.sum_of_unmarked(nums)}
                if no_win:
                    first = latest
                    no_win = False
                to_remove.add(bricka)
        brickor.difference_update(to_remove)
        if not brickor:
            return first, latest

with open("input.txt") as f:
    input = f.readlines()
    print(partboth(input))
