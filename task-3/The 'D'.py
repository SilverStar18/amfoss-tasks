mat_size = int(input())

num = int(mat_size / 2)

if (mat_size == 1) :
    
    print('D')

for row in range(mat_size) :
    
    if (row < num ) :
        
        for x in range(num - row) :
            
            print('*', end = '')
            
        for y in range((2 * row) + 1) :
            
            print('D', end = '')
            
        for z in range(num - row) :
            
            print('*', end = '')
            
        print()
            
    elif (row == num) :
        
        print('D' * mat_size)
            
            
    else :
        
        for x in range(row - num) :
            
            print('*', end = '')
            
        for y in range((2 * (mat_size - row)) - 1) :
            
            print('D', end = '')
            
        for z in range(row - num) :
            
            print('*', end = '')
            
        print()