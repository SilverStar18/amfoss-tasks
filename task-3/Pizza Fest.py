x, y = input().split()

house = list(map(int, input().split()))
owner = list(map(int, input().split()))

address = dict((h, k) for h, k in enumerate(house, 1))

for x in owner :
    try :
        add = max(h for h, k in address.items() if k == x )
        print(add, end = ' ')
        address.pop(add)
        
    except :
        print('-1', end = ' ')
        