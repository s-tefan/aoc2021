def input(file_name):
    points = set()
    folds = []
    with open(file_name) as f:
        s = f.readlines()
        for line in s:
            if not line.strip():
                 break
            points.add( tuple(int(x) for x in line.strip().split(',')) )
        for line in s:
            words = line.strip().split()
            if len(words) == 3:
                if words[:2] == ["fold", "along"]:
                    folds.append((words[2][0],int(words[2][2:])))
    return {"points": points, "folds": folds}

def fold_set(point_set, fold):
    fold_dim = {"x": 0, "y": 1}[fold[0]]
    fold_line = fold[1]
    new_point_set = set()
    mini = min({x[fold_dim] for x in point_set})
    maxi = max({x[fold_dim] for x in point_set})
    offset = 0 if maxi - fold_line <= fold_line - mini else maxi + mini - 2*fold_line
    for point in point_set:
        new_point = list(point)
        if point[fold_dim] > fold_line:
            new_point[fold_dim] = 2*fold_line - point[fold_dim] + offset
            new_point_set.add(tuple(new_point))
        else:
            new_point[fold_dim] += offset
            new_point_set.add(tuple(new_point))
    return new_point_set


def partone(data):
    points = data["points"]
    folds = data["folds"]
    print('points:', points)
    print('folds:', folds)
    fold = folds[0]
    points = fold_set(points, fold)
    return(points)


def parttwo(data):
    points = data["points"]
    folds = data["folds"]
    print('points:', points)
    print('folds:', folds)
    for fold in folds:
        points = fold_set(points, fold)
    xmax = max({x[0] for x in points})
    ymax = max({x[1] for x in points})
    display = ["."*(xmax + 1)]*(ymax + 1)
    for point in points:
        x = point[0]
        s = display[point[1]]
        display[point[1]] = s[:x]+"#"+s[x+1:]
    return display

data = input("input.txt")
print(len(partone(data)))
display_list = parttwo(data)
for line in display_list:
    print(line)
