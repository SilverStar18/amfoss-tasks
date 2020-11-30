
def pair_sum(n, s, array) :
    
    for x in range(n) :

        for y in range(x + 1, n):

            if (array[x] + array[y] == s) :
                
                return True
            
    return False


num_ele, req_sum = map(int, input().split())

int_lst = list(map(int, input().split()))

print(pair_sum(num_ele, req_sum, int_lst))
  
