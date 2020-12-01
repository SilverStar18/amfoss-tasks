def funcincredible(n) :
    
    inc_ser = [0, 1, 2]
    x = 0
    
    while (x < n) :
        
        inc_n = ((sum(inc_ser)) % 1000000007)
        inc_ser.append(inc_n)
        inc_ser.pop(0)
        x += 1
    
    return inc_ser[0]

T_case = int(input())

for x in range(T_case) :
    
    Term = int(input())
    
    nth_Term = str(funcincredible(Term))
    
    rev_Term = int((nth_Term)[::-1])
    
    print (rev_Term)
    
    
        
