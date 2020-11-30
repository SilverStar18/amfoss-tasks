n = int(input())

string = str(input())

binary_str = list(map(int, string))

n_zero = 0

n_one = 0

for x in binary_str :
    
    if (x == 0) :
        
        n_zero += 1
        
    else :
        
        n_one += 1
        

if (n_zero == n_one) :
    
    print("2")
    
else :
    
    print("1")