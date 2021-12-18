class SnailfishNumber(list):
    @classmethod
    def sum(a, b):
        return [a,b]

    def reduce(self, level = 0):
        if level >=4:
            pass

    def magnitude(self):
        a, b = self
        if isinstance(a, SnailfishNumber):
            c = 3*a.magnitude()
        else:
            c = 3*a
        if isinstance(b, SnailfishNumber):
            d = 2*b.magnitude()
        else:
            d = 2*b
        return c+d

class SFN:
    def __init__(self):
        self.nodelist = []

    def read(self, s):
        self.nodelist = []
        pf = ""
        for c in s:
            if  c == "[":
                pf = pf + "L"
            elif  c == ",":
                    pf = pf + "R"
            elif  c in {"0","1","2","3","4","5","6","7","8","9"}:
                    self.nodelist.append({"track": pf, "number": int(c)})
                    pf = pf[:-1]
            elif  c == "]":
                    pf = pf[:-1]
        return self


    def explode(self, pos):
        # po is teh position in nodelist of the left number of a pair
        if self.nodelist[pos]["track"][:-1] != self.nodelist[pos + 1]["track"][:-1]:
            raise Exception("Not a regular number pair at pos {}: {}".format(
                pos, self.nodelist[pos:pos+2]))
        if pos > 0:
            self.nodelist[pos - 1]["number"] += self.nodelist[pos]["number"]
        if pos < len(self.nodelist) - 2:
            self.nodelist[pos + 2]["number"] += self.nodelist[pos + 1]["number"]
        self.nodelist = self.nodelist[:pos] + \
            [{"track": self.nodelist[pos]["track"][:-1], "number": 0}] + \
            self.nodelist[pos+2:]
        return self

    def split(self, pos):
        n = self.nodelist[pos]["number"]
        t = self.nodelist[pos]["track"]
        a, b = n//2, n - n//2
        self.nodelist = self.nodelist[:pos] + \
            [{"track": t + "L", "number": a}, {"track": t + "R", "number": b}] + \
            self.nodelist[pos+1:]

    @classmethod
    def sum(cls, a, b):
        result = SFN()
        if a.nodelist and b.nodelist:
            nl_a = [{"track": "L" + x["track"], "number": x["number"]} for x in a.nodelist]
            nl_b = [{"track": "R" + x["track"], "number": x["number"]} for x in b.nodelist]
            result.nodelist = nl_a + nl_b
            return result
        elif a.nodelist:
            result.nodelist = list(a.nodelist)
        else:
            result.nodelist = list(b.nodelist)
        return result

    def reduced(self):
        '''Reduce self once, return True if reduced.'''
        for pos, node in enumerate(self.nodelist):
            if len(node['track']) > 4:
                self.explode(pos)
                return False
        for pos, node in enumerate(self.nodelist):
            if node['number'] >= 10:
                self.split(pos)
                return False
        return True

    def reduce(self):
        while (not self.reduced()):
            pass


def main():
    with open("test.txt") as f:
        s = SFN()
        n = SFN()
        for line in f.readlines():
            n.read(line.strip())
            print("n:", n.nodelist)
            s = SFN.sum(s,n)
            print("s:", s.nodelist)
            s.reduce()
            print("sred:", s.nodelist)
        #print(s.magnitude())


main()

'''
# [[[[4,3],4],4],[7,[[8,4],9]]] + [1,1]
bepa = SFN()
bepa.read("[[[[4,3],4],4],[7,[[8,4],9]]]")
print(bepa.nodelist)
cepa = SFN()
cepa.read("[1,1]")
print(cepa.nodelist)
depa = SFN.sum(bepa, cepa)
depa.reduce()
print(depa.nodelist)

'''
'''

SN = SnailfishNumber

apa = SN([SN([1,2]),SN([SN([3,4]),5])])
print(apa.magnitude())
'''
