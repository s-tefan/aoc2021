def main():
    template, rules = input("input.txt")
    print(partone(template, rules, 10))
    print(parttwo(template, rules, 10))
    print(parttwo(template, rules, 40))

def input(file_name):
    with open(file_name) as f:
        template = f.readline().strip()
        f.readline()
        rules = {}
        for line in f.readlines():
            s = line.strip().split(" -> ")
            rules[s[0]] = s[1]
        return template, rules

def iterate(template, rules, n):
    old_string = template
    for k in range(n):
        last_letter = old_string[0]
        new_string = last_letter
        for letter in old_string[1:]:
            if last_letter + letter in rules:
                new_string += rules[last_letter + letter] + letter
            else:
                new_string += letter
            last_letter = letter
        old_string = new_string
        apa = [new_string[k]+new_string[k+1] for k in range(len(new_string)-1)]
    return new_string

def partone(template, rules, n):
    """The naïve approach which works for part one but not reasonably
    for part two as it scales exponentially."""
    atoms = set(template)
    for rule in rules:
        atoms.add(rules[rule])
    polymer = iterate(template, rules, n)
    numbers = [polymer.count(x) for x in atoms]
    return max(numbers) - min(numbers)

def increase_counter(dictionary, key, n):
    if key in dictionary:
        dictionary[key] += n
    else:
        dictionary[key] = n

def parttwo(template, rules, n):
    """Better scalability by storing data as a dict of digraph frequencies"""
    first, last = template[0], template[-1]
    atoms = set(template)
    for rule in rules:
        atoms.add(rules[rule])
    digraphs = [template[k] + template[k+1] for k, _ in enumerate(template[:-1])]
    digraph_count = {}
    for d in digraphs:
        increase_counter(digraph_count, d, 1)
    for k in range(n):
        new_digraph_count = {}
        for digraph in digraph_count:
            if digraph in rules:
                increase_counter(new_digraph_count, digraph[0] + rules[digraph], digraph_count[digraph])
                increase_counter(new_digraph_count, rules[digraph] + digraph[1], digraph_count[digraph])
            else:
                increase_counter(new_digraph_count, digraph, digraph_count[digraph])
        digraph_count = new_digraph_count
    atom_count_twice = {}
    # count characters in digraphs, each character, except in the ends, is counted twice
    for digraph in digraph_count:
        increase_counter(atom_count_twice, digraph[0], digraph_count[digraph])
        increase_counter(atom_count_twice, digraph[1], digraph_count[digraph])
    # First and last character were only counted atom_count_twice
    increase_counter(atom_count_twice, first, 1)
    increase_counter(atom_count_twice, last, 1)
    return (max(atom_count_twice.values()) - min(atom_count_twice.values()))//2

main()
