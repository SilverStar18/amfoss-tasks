import functools

def reward(n, k, num) :
    
    num.sort()
    
    num[n-1] = num[n-1] - k
    
    money = functools.reduce((lambda bg1, bg2 : bg1 * bg2), num)
    
    return money

tst_case = int(input())

for x in range(tst_case) :
    
    num_bags, money_ret = map(int, input().split())

    bags = list(map(int, input().split()))
    
    print(reward(num_bags, money_ret, bags))

