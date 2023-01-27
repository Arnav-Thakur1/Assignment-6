class Sum0:
    def output():
        n=int(input("Enter the number of elements in the input array\n"))
        l_1=[]
        for i in range(n):
            temp=int(input(f"Enter the number({i+1}) \n"))
            l_1.append(temp)
        def find_3_tuples(l_1):
            l_2=[]
            for i in l_1:
                for j in l_1:
                    for k in l_1:
                        if i+j+k==0:
                            l_2.append([i,j,k])
            l_3=list(set(tuple(sorted(sub)) for sub in l_2))
            return [l_3]
        print(find_3_tuples(l_1))
    
Sum0.output()