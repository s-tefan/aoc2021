depths = [int(x) for x in open("input.txt")]
print([(depths[n+1]-depths[n]) > 0 for n in range(len(depths)-1)].count(True),[(depths[n+3]-depths[n]) > 0 for n in range(len(depths)-3)].count(True))