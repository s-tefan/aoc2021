
class SFN_sub(list):
    def __init__(self, nodelist = []):
        self = nodelist

    def read(self, s):
        pf = ""
        for c in s:
            if  c == "[":
                pf = pf + "L"
            elif  c == ",":
                pf = pf + "R"
            elif  c in {"0","1","2","3","4","5","6","7","8","9"}:
                self.append({"track": pf, "number": int(c)})
                pf = pf[:-1]
            elif  c == "]":
                pf = pf[:-1]
        return self


    def explode(self, pos):
        # po is teh position in nodelist of the left number of a pair
        if self[pos]["track"][:-1] != self[pos + 1]["track"][:-1]:
            raise Exception("Not a regular number pair at pos {}: {}".format(
                pos, self[pos:pos+2]))
        if pos > 0:
            self[pos - 1]["number"] += self[pos]["number"]
        if pos < len(self) - 2:
            self[pos + 2]["number"] += self[pos + 1]["number"]
        self = self[:pos] + \
            [{"track": self[pos]["track"][:-1], "number": 0}] + \
            self[pos+2:]
        return self

    def split(self, pos):
        n = self[pos]["number"]
        t = self[pos]["track"]
        a, b = n//2, n - n//2
        self = self[:pos] + \
            [{"track": t + "L", "number": a}, {"track": t + "R", "number": b}] + \
            self[pos+1:]


    def add(self, b):
        if len(self) > 0 and len(b) > 0:
            nl_a = [{"track": "L" + x["track"], "number": x["number"]} for x in self]
            nl_b = [{"track": "R" + x["track"], "number": x["number"]} for x in b]
            self = SFN(nl_a + nl_b)
            print(type(self))
            print(self)
            print("Kuken!")
        elif len(self) > 0:
            pass
        else:
            self = SFN(b)

    @classmethod
    def sum(cls, a, b):
        if len(a) > 0 and len(b) > 0:
            nl_a = [{"track": "L" + x["track"], "number": x["number"]} for x in a]
            nl_b = [{"track": "R" + x["track"], "number": x["number"]} for x in b]
            result = SFN(nl_a + nl_b)
        elif len(a) > 0:
            result = SFN(a)
        else:
            result = SFN(b)
        return reduce()


    def reduced(self):
        '''Reduce self once, return True if reduced.'''
        for pos, node in enumerate(self):
            if len(node['track']) > 4:
                self.explode(pos)
                return False
        for pos, node in enumerate(self):
            if node['number'] >= 10:
                self.split(pos)
                return False
        return True

    def reduce(self):
        while (not self.reduced()):
            pass
