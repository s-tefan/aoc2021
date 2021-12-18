class CaveSystem:
    def __init__(self, file_name = None):
        self.passages = set()
        self.small_caves = set()
        self.large_caves = set()
        if file_name:
            with open(file_name) as f:
                for line in f.readlines():
                    self.add_edge(line.strip().split('-'))

    def add_edge(self, e):
        e = tuple(e)
        a, b = e
        self.add_cave(a)
        self.add_cave(b)
        self.passages.add(e)

    def add_cave(self, c):
        if c[0].isupper():
            self.large_caves.add(c)
        elif c[0].islower():
            self.small_caves.add(c)
        else:
            raise(Exception("Cave name exception"))

    def remainder(self, start):
        rem = CaveSystem()
        rem.small_caves = set(self.small_caves)
        rem.small_caves.discard(start)
        rem.large_caves = self.large_caves
        rem.passages = set(self.passages)
        for cave in self.small_caves | self.large_caves:
            rem.passages.discard((start, cave))
            rem.passages.discard((cave, start))
        return rem

    def passages_to(self, start):
        return [b for (a,b) in self.passages if a == start] +\
            [a for (a,b) in self.passages if b == start]

    def is_empty(self):
        return not self.passages

    def __str__(self):
        return "Small caves: {}\nLarge caves: {}\nPassages: {}".format(
            self.small_caves,
            self.large_caves,
            self.passages)

    def count(self, start, end):
        if start == end:
            return 1
        else:
            next_caves = self.passages_to(start)
            if start in self.large_caves:
                ways_to_go = [(next_cave, self) for next_cave in next_caves]
            elif start in self.small_caves:
                ways_to_go = [(next_cave, self.remainder(start)) for next_cave in next_caves]
            else:
                raise(Exception("För fan"))
            return sum(rem.count(c, 'end') for (c, rem) in ways_to_go)

    def count2(self, start, end, bullet, visited_in):
        visited = set(visited_in)
        if start == end:
            return 1
        else:
            next_caves = self.passages_to(start)
            if start in self.large_caves:
                ways_to_go = [(next_cave, self) for next_cave in next_caves]
                return sum(rem.count2(c, 'end', bullet, visited) for (c, rem) in ways_to_go)
            elif start in self.small_caves:
                if start == "start":
                    ways_to_go = [(next_cave, self.remainder(start)) for next_cave in next_caves]
                    return sum(rem.count2(c, 'end', bullet, visited) for (c, rem) in ways_to_go)
                elif start in visited:
                    if bullet:
                        # fire at monster
                        ways_to_go = [(next_cave, self.remainder(start)) for next_cave in next_caves]
                        return sum(rem.count2(c, 'end', False, visited) for (c, rem) in ways_to_go)
                    else:
                        return 0
                else:
                    visited.add(start)
                    ways_to_go = [(next_cave, self) for next_cave in next_caves]
                    return sum(rem.count2(c, 'end', bullet, visited) for (c, rem) in ways_to_go)
            else:
                raise(Exception("För fan"))

cs = CaveSystem("input.txt")
print(cs.count('start', 'end'))
#print(cs.count2('start', 'end', False, set()))
print(cs.count2('start', 'end', True, set()))
