def optimize1sort(crabpos):
    '''sum(abs(x-a) for x in crabpos) is optimized by a being a median of crabpos.'''
    crabpos.sort()
    n_crabs = len(crabpos)
    opt = crabpos[n_crabs//2]
    return opt, sum(abs(x-opt) for x in crabpos)

def optfun(crabpos, a):
    return sum(abs(x-a)*(abs(x-a)+1)/2 for x in crabpos)

'''Optimized by a where 
n*a - sum(x for x in crabpos) - sum(sgn(x-a) for x in crabpos)/2 == 0
approximated by a = sum(x[i])/n.'''

def sgn(x):
    return int(x>0) - int(x<0)

def optimize2(crabpos):
    a = sum(crabpos)/len(crabpos) # arithmetic mean optimizes squared distance sum, approx. for this
    a += sum(sgn(x-a) for x in crabpos)/2/len(crabpos) # adjust a little, hopefully (and in fact) getting better approx
    if verbose: print('Computed fp optimum:', a, optfun(crabpos, a))
    if verbose: print('Environment:', {aa: optfun(crabpos, aa) for aa in (a-0.02, a-0.01, a, a+0.01, a+0.02)}) # checking some values in the environment of a
    b, c = (optfun(crabpos, int(a)), optfun(crabpos, int(a)+sgn(a)))
    return (int(a),int(b)) if b <= c else (int(a)+sgn(a),int(c))
    # hopefully this gives the true optimal integer, should really check by stepping ...

verbose = True
test = [16,1,2,0,4,2,7,1,2,14]
print("Test set ({})".format(len(test)))
print('1:', optimize1sort(test))
print('2:', optimize2(test))
with open("input.txt") as f:
    input = [int(x) for x in f.readline().split(',')]
print("Input set ({})".format(len(input)))
print('1:', optimize1sort(input))
print('2:', optimize2(input))

