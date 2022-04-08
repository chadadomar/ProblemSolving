def test(w,h,L):
    ligne=1
    som=0
    for k in range(len(L)):
        som+=L[k]
        if ligne > h : break
        if som > w : 
            print('NO')
            break
        if som==w:
            if ligne==h:
                print('YES')
                break
            ligne+=1
            som=0
    if som<w : print('NO')
