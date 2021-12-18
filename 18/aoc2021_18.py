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

    def __str__(self):
        return str(self.nodelist)

    def magnitude(self):
        nl = self.nodelist
        if len(nl) == 1:
            return int(nl[0]["number"])
        else:
            L = SFN()
            R = SFN()
            L.nodelist = [{"track": x["track"][1:], "number": x["number"]}
                    for x in nl if x["track"][0] == "L"]
            R.nodelist = [{"track": x["track"][1:], "number": x["number"]}
                    for x in nl if x["track"][0] == "R"]
            return 3*L.magnitude() + 2*R.magnitude()

def partone(filename):
    with open(filename) as f:
        s = SFN()
        s.read(f.readline().strip())
        for line in f.readlines():
            n = SFN()
            n.read(line.strip())
            s = SFN.sum(s,n)
            s.reduce()
        print(s.magnitude())

def parttwo(filename):
    with open(filename) as f:
        sfn_list = []
        for line in f.readlines():
            n = SFN()
            n.read(line.strip())
            sfn_list.append(n)
        mag_list = []
        for a in sfn_list:
            for b in sfn_list:
                if a != b:
                    s = SFN.sum(a,b)
                    s.reduce()
                    mag_list.append(s.magnitude())
        print(max(mag_list))


partone("input.txt")
parttwo("input.txt")
