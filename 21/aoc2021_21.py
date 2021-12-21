def main(a,b):
    print(partone(a,b))

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
        #print("Player {} at {} has new score {}".format(k+1, player[k].position_minus_one + 1, player[k].score))
        if player[k].score >= endscore:
            break
        k = 1 - k
    print('Player {} won with score {} while player {} just had score {}'.format(k + 1, player[k].score, 2 - k, player[1-k].score))
    return(player[1-k].score * 3*n)

main(3,5)