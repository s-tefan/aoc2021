
class BitString:
    def __init__(self, s):
        self.string = s

    def pop(self, n):
        x = int(self.string[:3], 2)
        self. string = self.string[3:]
        return x

    def pushbit(self, b):
        if b:
            self.string = "1" + self.string
        else:
            self.string = "0" + self.string

    def readpacket(self):
        version = self.pop(3)
        id = self.pop(3)
        match id:
            case 4:
                apa = 0
                while self.pop(1) == 1:
                    apa +<< 4
                    apa += self.pop(4)
                apa +<< 4
                apa += self.pop(4)
                while next(dataiter == 0):
                    pass
                self.pushbit(1)
            case _:
                mode = self.pop(1)
                match mode:
                    case 0:
                        length = self.pop(15)
                    case 1:
                        number = self.pop(11)


def main():
    with open("input.txt") as f:
        hexdata = f.readline().strip()
        f.close()
    bs = BitString(hex_to_binary(hexdata)))



def hex_to_binary(s):
    """recode hexdigit for hexdigit"""
    binstring = ""
    for c in s:
        binstring += "{:04b}".format(int(c, 16))
    return binstring


main()
