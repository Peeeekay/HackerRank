def flag_1(x,y,n):
    chose = (x^lastAnswer) % n
    main[chose].append(y)

def flag_2(x,y,n):
    chose = (x^lastAnswer) % n
    size = len(main[chose])
    index = y % size
    return main[chose][index]
    
main = []
lastAnswer = 0
first = raw_input().split()
n = int(first[0])
q = int(first[1])

for i in range(n):
    main.append([])

i = 0
while i < q:
    query = raw_input().split()
    flag = query[0]
    x = int(query[1])
    y = int(query[2])
    if flag == "1":
        flag_1(x,y,n)
    else:
        lastAnswer = flag_2(x,y,n)
        print lastAnswer
    i = i + 1
