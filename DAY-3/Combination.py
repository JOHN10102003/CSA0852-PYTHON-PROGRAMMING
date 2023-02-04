def combination(l):
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if(i!=j and j!=k and i!=k):
                    print(l[i],l[j],l[k])
combination([1,2,3])
