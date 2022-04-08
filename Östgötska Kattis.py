s=input().split()
k=len(s)
count=0
for i in range(k):
    #print("i ",i)
    c=s[i]
    for j in range(len(c)):
        #print(c[j:j+2])
        if c[j:j+2]=="ae":
            count+=1
            break
#print("count ",count)
#print("k ",k)
if count>= 0.4*k:
    print("dae ae ju traeligt va")
else:
    print("haer talar vi rikssvenska")