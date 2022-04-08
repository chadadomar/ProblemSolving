x,y=[int(k) for k in  input().split()]
while x+y!=0:
    if x+y==13:
        print("Never speak again.")
    elif x>y:
        print("To the convention.")
    elif x<y:
        print("Left beehind.")
    else:
        print("Undecided.")
    x,y=[int(k) for k in  input().split()]
