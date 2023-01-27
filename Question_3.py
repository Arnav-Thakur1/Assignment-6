list_1=[]
list_2=[]
def nth_row(n):
    global list_1,list_2
    if n==1:
        list_1=[1]
    elif n==2:
        list_1=[1,2,1]
    else:
        nth_row(n-1)
        list_2=[1]
        for i in range(len(list_1)-1):
            list_2.append(list_1[i]+list_1[i+1])
        list_2.append(1)
        list_1=list_2
    return list_1

n=int(input("Enter the number of rows of Pascal Triangle you want to print"))

for i in range(1,n+1):
    print(' '*(n-i),end='')
    nth_row(i)
    for j in list_1:
        print(j,end=' ')
    print()