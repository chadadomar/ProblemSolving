l=[int(k) for k in input().split()]
ch=input()
L=sorted(l)
D={'A':L[0],'C':L[2],'B':L[1]}
print(D[ch[0]],' ',D[ch[1]],' ',D[ch[2]])
 


            