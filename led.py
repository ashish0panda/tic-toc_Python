def display(draw):
    m=3
    n=0
    for k in range(5):
        j=0
        for i in range(0,len(draw)):
            for j in range(n,m):
                print(draw[i][j],end='')
                j+=1
            print("",end='  ')
        n=m
        m+=3
        print()
            
                
        
def convertor(strng):
    lst=[" " for i in range(15)]
    if strng=="1":
        temp=[2,5,8,11,14]
        for i in temp:
            lst[i]="#"
    elif strng=="2":
        temp=[0,1,2,5,6,7,8,9,12,13,14]
        for i in temp:
            lst[i]="#"
    elif strng=="3":
        temp=[0,1,2,5,6,7,8,11,12,13,14]
        for i in temp:
            lst[i]="#"
    elif strng=="4":
        temp=[0,2,3,5,6,7,8,11,14]
        for i in temp:
            lst[i]="+"
    elif strng=="5":
        temp=[0,1,2,3,6,7,8,11,12,13,14]
        for i in temp:
            lst[i]="#"
    elif strng=="6":
        temp=[0,1,2,3,6,7,8,9,11,12,13,14]
        for i in temp:
            lst[i]="#"
    elif strng=="7":
        temp=[0,1,2,5,8,11,14]
        for i in temp:
            lst[i]="#"
    elif strng=="8":
        temp=[0,1,2,3,5,6,7,8,9,11,12,13,14]
        for i in temp:
            lst[i]="#"
    elif strng=="9":
        temp=[0,1,2,3,5,6,7,8,11,12,13,14]
        for i in temp:
            lst[i]="#"
    else:
        temp=[0,1,2,3,5,6,8,9,11,12,13,14]
        for i in temp:
            lst[i]="#"
    return(lst)

        
num=input("Enter your number:")
word_hash=[]
for word in num:
    word_hash.append(convertor(word))
display(word_hash)
    
        
