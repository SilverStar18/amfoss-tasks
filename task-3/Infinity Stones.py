def transfer(N, K, lst) :
    
    lst.sort(reverse = True)
    
    mx_box = [lst[z] for z in range(K)]
    
    max_prtct = sum(mx_box)
    
    return (max_prtct >= N)


tst_case = int(input())

for x in range(tst_case) :
    
    stn, box, s_box = map(int, input().split())
    
    stones = list(map(int, input().split()))
    
    max_cap = list(map(int, input().split()))
    
    if (s_box >= box) :
        
        print("YES")
        
    else :
        
        if transfer(stn, s_box, max_cap) :
            
            print("YES")
            
        else :
            
            print("NO")
    
