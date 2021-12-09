def partone(input_lines):
    s = 0
    for line in input_lines:
        _, b = line.split(' | ')
        s += sum([len(x) for x in b.split()].count(n) for n in {2, 4, 3, 7})
    return(s)


def sorted_string(s):
    return ''.join(sorted(s))


def addsym(d, a, b):
    d[a] = b
    d[b] = a


def parttwo(input_lines):
    s = 0
    for line in input_lines:
        a, b = line.split(' | ')
        aa = [sorted_string(x) for x in a.split()]
        digit_dict = {}  # will map in both ways
        unique = {2: 1, 3: 7, 4: 4, 7: 8}
        for k, m in unique.items():
            addsym(digit_dict, m, next(x for x in aa if len(x) == k))
        addsym(digit_dict, 6, next(x for x in aa if 
            x not in digit_dict and 
            len(set(x) & set(digit_dict[1])) == 1 and 
            len(x) == 6))
        addsym(digit_dict, 5, next(x for x in aa if 
            x not in digit_dict and 
            len(set(x) & set(digit_dict[1])) == 1 and 
            len(set(x) & set(digit_dict[4])) == 3))
        addsym(digit_dict, 2, next(x for x in aa if 
            x not in digit_dict and 
            len(set(x) & set(digit_dict[1])) == 1 and 
            len(set(x) & set(digit_dict[4])) == 2))
        addsym(digit_dict, 3, next(x for x in aa if 
            x not in digit_dict and 
            len(x) == 5))
        addsym(digit_dict, 9, next(x for x in aa if 
            x not in digit_dict and 
            len(set(x) & set(digit_dict[4])) == 4))
        addsym(digit_dict, 0, next(x for x in aa if 
            x not in digit_dict and 
            len(set(x) & set(digit_dict[4])) == 3))
        s += int(''.join(str(digit_dict[sorted_string(digit)])
                 for digit in b.split()))
    return(s)


with open("input.txt") as f:
    input_lines = [line.strip() for line in f.readlines()]
    print(partone(input_lines))
    print(parttwo(input_lines))
