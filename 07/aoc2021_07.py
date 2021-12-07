def optimize1sort(crabpos):
    '''sum(abs(x-a) for x in crabpos) is optimized by a being a median of crabpos.'''
    crabpos.sort()
    n_crabs = len(crabpos)
    opt = crabpos[n_crabs//2]
    return opt, sum(abs(x-opt) for x in crabpos)

def optfun(crabpos, a):
    return int(sum(abs(x-a)*(abs(x-a)+1)/2 for x in crabpos))

'''Optimized by a where 
n*a - sum(x for x in crabpos) - sum(sgn(x-a) for x in crabpos)/2 == 0
approximated by a = sum(x[i])/n.'''

def sgn(x):
    return int(x>0) - int(x<0)

def optimize2(crabpos):
    a = sum(crabpos)/len(crabpos) # arithmetic mean optimizes squared distance sum, approx. for this
    a += sum(sgn(x-a) for x in crabpos)/2/len(crabpos) # adjust a little, hopefully getting better approx
    print(a, optfun(crabpos, a))
    b, c = (optfun(crabpos, int(a)), optfun(crabpos, int(a+1)))
    return (int(a),b) if b <= c else (int(a)+sgn(a),c)
    # hopefully this gives the true optimal integer, should really check by stepping ...

test = [16,1,2,0,4,2,7,1,2,14]
print("Test set ({})".format(len(test)))
print(optimize1sort(test))
print(optimize2(test))
with open("input.txt") as f:
    input = [int(x) for x in f.readline().split(',')]
print("Input set ({})".format(len(input)))
print(optimize1sort(input))
print(optimize2(input))

