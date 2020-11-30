n = int(input())

req_paper = list(map(int, input().split()))
 
given_paper = list(map(int, input().split()))
  
types = []

for i in range(n) :
  
  types.append(given_paper[i]/req_paper[i])

poss_books = list(map(int, types))

Dnote = min(poss_books)

print(Dnote)  
