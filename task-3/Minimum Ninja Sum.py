def mns(n, k) :
    
    if (len(n) <= k) :
        return -1
    
    else :
        
        lst = list(map(int, n))
        
        d = abs(lst[0] - lst[k])
        
        for x in range(len(n) - k) :
            
            d = min(d, abs(lst[x] - lst[x + k]))
            
        return d

tst_cs = int(input())

for t in range(tst_cs) :
    
    n, p = input().split()
    k = int(p)
    print(mns(n, k))

    
    