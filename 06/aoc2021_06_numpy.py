import numpy

with open("input.txt") as f:
    input = f.readline()
fish_timers_init = [int(x) for x in input.strip().split(',')]
n = 8
nos = [0]*(n+1)
for k in fish_timers_init:
    nos[k] += 1
a = numpy.array(
        [[0,1,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,0,0,0],
        [0,0,0,1,0,0,0,0,0],
        [0,0,0,0,1,0,0,0,0],
        [0,0,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,1,0,0],
        [1,0,0,0,0,0,0,1,0],
        [0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0]
    ])
w, v = numpy.linalg.eig(a)
print(round(abs(sum(v@numpy.linalg.matrix_power(numpy.diag(w), 80)@numpy.linalg.inv(v)@nos))))
print(round(abs(sum(v@numpy.linalg.matrix_power(numpy.diag(w), 256)@numpy.linalg.inv(v)@nos))))