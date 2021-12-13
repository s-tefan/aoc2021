file_name = "test.txt"
with open(file_name) as f:
    points = {(tuple(int(x) for x in line.strip().split(',')))\
        for line in f.readlines()}
print(points)
