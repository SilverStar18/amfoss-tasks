def Prod(mat1, mat2) :
    
    matrix = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    
    for x in range(3) :
        for y in range(3) :
            for z in range(3) :
                
                matrix[x][y] += mat1[x][z] * mat2[z][y]
                
    for x in range(3) :
        for y in range(3) :
            
            mat1[x][y] = matrix[x][y]


def funcIncredible(mat, n) :
    
    P = [[1, 1, 1],
         [1, 0, 0],
         [0, 1, 0]]
    
    if (n == 1) :
        
        return mat
    
    funcIncredible(mat, int(n / 2))
    
    Prod(mat, mat)
    
    if not (n % 2 == 0) :
        
        Prod(mat, P) 
    

def Incredible(n) :
    
    IncMat = [[1, 1, 1],
              [1, 0, 0],
              [0, 1, 0]]
    
    funcIncredible(IncMat, n)
    
    return IncMat[0][1]


T_case = int(input())

for x in range(T_case) :
    
    Term = int(input())
    
    nth_Term = Incredible(Term) % 1000000007
    
    rev_Term = int(str(nth_Term)[::-1])
    
    print (rev_Term)
    
    
        