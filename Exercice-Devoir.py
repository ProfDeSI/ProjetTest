def mini(M):
    L=[]
    for x in M:
        for y in x:
            L.append(y)
    return min(L)

def oppose(M):
    l=[]
    for x in range(len(M)):
        l.append([])
        for y in M[x]:
            l[x].append(-y)
    return l

def maxi(M):
    L=oppose(M)
    maximum=-mini(L)
    return maximum

def extremums(M):
    l=(mini(M),maxi(M))
    return l

print(extremums([[3,2,1],[4,-4,0],[7,8,9]]))
