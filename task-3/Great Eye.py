def sum_ascii(n) :

    for x in range(n) :

        wrd_pos = int(input())

        stat = list(map(str, input().split()))

        if wrd_pos in range(len(stat)) :

            sum_wrd = sum(map(ord, stat[wrd_pos]))

            print(sum_wrd)

        else :

            print("-1")
        
tst_case = int(input())

sum_ascii(tst_case)