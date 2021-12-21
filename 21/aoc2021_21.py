import math

def main(a,b):
    print('Part 1:', partone(a,b))
    print('Part 2:', parttwo(a,b))


class Player:
    def __init__(self, start):
        self.position_minus_one = start - 1
        self.score = 0
    def update(self, dice):
        for k in range(3):
            diceroll = dice.roll()
            self.position_minus_one += diceroll
            self.position_minus_one %= 10
        self.score += (self.position_minus_one + 1)

    def updated2(self, k):
        newplayer = Player(0)
        newplayer.position_minus_one = (self.position_minus_one + k) % 10
        newplayer.score = self.score + newplayer.position_minus_one + 1
        return newplayer
    def copy(self):
        newplayer = Player(1 + self.position_minus_one)
        newplayer.score = self.score
        return(newplayer)


class DeterministicDice:
    def __init__(self, modulo):
        self.value = 0
        self.modulo = modulo
    def roll(self):
        self.value %= self.modulo
        self.value += 1
        return self.value


def partone(a,b):
    endscore = 1000
    player = [Player(a), Player(b)]
    dice = DeterministicDice(100)
    k = 0 # player(-1) in turn
    n = 0 # number of halfrounds played
    while True:
        n += 1
        player[k].update(dice)
        if player[k].score >= endscore:
            break
        k = 1 - k
    print('Player {} won with score {} while player {} just had score {}'.format(k + 1, player[k].score, 2 - k, player[1-k].score))
    return(player[1-k].score * 3*n)


def parttwo(a,b):
    win = 21
    round_steps = {3,4,5,6,7,8,9}
    round_step_poss ={3:1,4:3,5:6,6:7,7:6,8:3,9:1}
    undecided = {(): [Player(a), Player(b)]}
    wins = [set(), set()]
    winsposs = [0,0]
    k = 0
    while undecided:
        nextundecided = {}
        for grej in undecided:
            for s in round_steps:
                newgrej = grej + (s,)
                new_playerpair = [None, None]
                new_playerpair[k] = undecided[grej][k].updated2(s)
                new_playerpair[1-k] = undecided[grej][1-k].copy()
                if new_playerpair[k].score >= win:
                    winsposs[k] += math.prod(round_step_poss[x] for x in newgrej)
                else:
                    nextundecided[newgrej] = new_playerpair
        undecided = nextundecided
        k = 1 - k
        print(len(undecided),winsposs)
    return(max(winsposs))

main(3,5)
