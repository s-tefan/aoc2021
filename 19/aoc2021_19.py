def main(filename):
    with open(filename) as f:
        scanners = {}
        lines = (rawline.strip() for rawline in f.readlines())
        while True:
            line = next(lines)
            if line[:3] == '---':
                _, _, k, _ = line.split()
                scanners[k] = set()
                while True:
                    line = next(lines)
                    print(line)
                    if line:
                        scanners[k].add(tuple(int(s) for s in next(lines).split(',')))
                    else:
                        break

main('input.txt')
