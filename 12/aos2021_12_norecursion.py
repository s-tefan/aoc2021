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

    def path_list1(self, start, end):
        """Return all finished paths according to part 1 rules."""
        path_list_unfinished = [[start]]
        path_list_finished = []
        while path_list_unfinished: # run as long as there is
            delta_list = []
            while path_list_unfinished: # until popped empty
                path = path_list_unfinished.pop(0) # pop
                for c in self.passages_to(path[-1]): # continue from last
                    new_path = list(path)
                    if c == end:
                        new_path.append(c)
                        path_list_finished.append(new_path)
                    elif c in self.large_caves or c not in path:
                        new_path.append(c)
                        delta_list.append(new_path)
            path_list_unfinished = delta_list
        return path_list_finished

    def path_list2(self, start, end):
        """Return all finished paths according to part 2 rules."""
        path_list_unfinished = [{'bullet': True, 'path': [start]}]
        path_list_finished = []
        while path_list_unfinished: # run as long as there is
            delta_list = []
            while path_list_unfinished: # until popped empty
                path = path_list_unfinished.pop(0) #

                for c in self.passages_to(path['path'][-1]): # continue from last
                    new_path = list(path['path'])
                    if c == end:
                        new_path.append(c)
                        path_list_finished.append({'bullet': path['bullet'], 'path': new_path})
                    elif c in self.large_caves or c not in new_path:
                        new_path.append(c)
                        delta_list.append({'bullet': path['bullet'], 'path': new_path})
                    elif path['bullet'] and c != start:
                        new_path.append(c)
                        delta_list.append({'bullet': False, 'path': new_path})
            path_list_unfinished = delta_list
        return path_list_finished

    def count_paths2(self, start, end):
        """Return number of finished paths, don't deliver them."""
        path_list_unfinished = [{'bullet': True, 'path': [start]}]
        n_path_list_finished = 0
        while path_list_unfinished: # run as long as there is
            delta_list = []
            while path_list_unfinished: # until popped empty
                path = path_list_unfinished.pop(0) #

                for c in self.passages_to(path['path'][-1]): # continue from last
                    new_path = list(path['path'])
                    if c == end:
                        new_path.append(c)
                        n_path_list_finished += 1
                    elif c in self.large_caves or c not in new_path:
                        new_path.append(c)
                        delta_list.append({'bullet': path['bullet'], 'path': new_path})
                    elif path['bullet'] and c != start:
                        new_path.append(c)
                        delta_list.append({'bullet': False, 'path': new_path})
            path_list_unfinished = delta_list
        return n_path_list_finished



cs = CaveSystem("input.txt")
#print(cs.count('start', 'end'))
#print(cs.count2('start', 'end', True, set()))
pathlist = cs.path_list1("start", "end")
print(len(pathlist))
#pathlist2 = cs.path_list2("start", "end")
print(cs.count_paths2("start", "end"))
