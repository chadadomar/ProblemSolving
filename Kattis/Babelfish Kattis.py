import sys
d = {}
s =input()
while s != '':
    t = s.split()
    d[t[1]] = t[0]
    s = input()

lines = sys.stdin.readlines()
for line in lines:
    if line[-1]=='\n':
        if line[:-1] in d.keys():
            print(d[line[:-1]])
        else:
            print('eh')
    else:
        if line in d.keys():
            print(d[line])
        else:
            print('eh')