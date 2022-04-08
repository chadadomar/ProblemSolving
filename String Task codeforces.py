c=input()
c="A"+c
c=c.capitalize()
c=c[1:]
l=["A","O","Y","E","U","I","a","o","y","e","u","i"]
for x in c:
    if x not in l:
        print('.'+x,end="")