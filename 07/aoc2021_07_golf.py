crabpos = sorted(int(x) for x in open("input.txt").readline().split(','))
print(sum([abs(x-crabpos[len(crabpos)//2]) for x in crabpos]))
a = sum(crabpos)/len(crabpos)
a += sum((int(x>a)-int(x<a)) for x in crabpos)/2/len(crabpos)
print((lambda a : int(sum(abs(x-a)*(abs(x-a)+1)/2 for x in crabpos)))(round(a)))