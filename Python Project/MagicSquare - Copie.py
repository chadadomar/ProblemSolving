

def ReadStore(name):
    try :
        file=open(name+".txt","r")
        
        l=file.readlines() #liste of lines (strings) in the file
        M=[]
        n=len(l[0].split()) #number of elements in the 1st row
        
        for i in range(len(l)) :
            o=l[i].split()
            if n!=len(o) :
                print("the",i+1,"th row havn't the same number of elements !")
                return []
            #if "." in o :
            #    print("there is a float number in the",i,"th row !")
            #    return []
            M.append(o)
        
        #M=[[int(k) for k in o.split()] for o in l]
        
        file.close()
        return M,l
    except :
        print("the file",name,"does not exist !")
        return [],[]

def isInt(c):
    for x in c:
        if not(x in "0123456789"):
            return False
    return True

def IsValid(M):
    n=len(M)
    for i in range(n):
        for j in range(n):
            if not(isInt(M[i][j])) :
                print("M["+str(i+1)+"]["+str(j+1)+"] isn't an integer !")
                return []
            elif (n*n<int(M[i][j]) or int(M[i][j])<1 ) :
                print("M["+str(i+1)+"]["+str(j+1)+"] isn't between 1 and",n*n)
                return []
            else :
                M[i][j]=int(M[i][j])
    return M

def Suml(l):
    s=0
    for x in l:
        s+=x
    return s

def SRow(M):
    s=Suml(M[0])
    i=0
    while i<len(M)-1 :
        i+=1
        if (s!=Suml(M[i])):
            #print("Row",i+1,"haven't the same sum as the previous ones")
            return 0,i
    return 1,s

def SCul(M):
    n=len(M)
    sumc=0
    for i in range(n):
        sumc+=M[i][0]
    for j in range(1,n):
        s=0
        for i in range(n):
            s+=M[i][j]
        if s!=sumc :
            #print("Column",j+1,"haven't the same sum as the previous ones")
            return 0,j
    return 1,sumc

def SDiag(M):
    n=len(M)
    s1=0
    for i in range(n):
        s1+=M[i][i]
    s2=0
    for i in range(n):
        s2+=M[i][n-1-i]
    if s1!=s2 :
        #print("the tow diagonals haven't the same sum")
        return 0
    else:
        return s1

name=input("hi, your square file name :")
N,l=ReadStore(name)
M=IsValid(N)

if M!=[] :
    if SRow(M)[0] :
        #print("the sums of each row are equall")
        S=SRow(M)[1]
        if SCul(M)[0] :
            #print("the sums ofeach column are equall")
            if SCul(M)[1]==S :
                if SDiag(M) :
                    #print("the sums of the tow diagonals are equall")
                    if SDiag(M)==S :
                        print("It's a magic square")
                        Vfile=open("VALID_"+name+".txt","w")
                        Vfile.writelines(l)
                        Vfile.close()
                    else :
                        print("the sum of diagonals are not equall to the sum of the rest (Rows,Column) ")
                else :
                    print("the diagonals haven't the same sum")
            else :
                print("the sum o f column is not equall to the sum of rows")
        else :
            j=SCul(M)[1]
            print("Column",j+1,"haven't the same sum as the previous ones")
    else :
        i=SRow(M)[1]
        print("Row",i+1,"haven't the same sum as the previous ones")

input("push a button to continue ...")
