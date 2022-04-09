a,b,c=[int(k) for k in input().split()]
n=str(a)
m=str(b)
q=str(c)
if a==b+c:
    print(n+'='+m+'+'+q)
elif a==b-c:
    print(n+'='+m+'-'+q)
    
elif a==b*c:
    print(n+'='+m+'*'+q)
   
elif a==b/c:
    print(n+'='+m+'/'+q)
   

elif c==b+a:
    print(n+'+'+m+'='+q)
    
elif c==a-b:
    print(n+'-'+m+'='+q)
    
elif c==b*a:
    print(n+'*'+m+'='+q)
    
elif c==a/b:
    print(n+'/'+m+'='+q)
    

