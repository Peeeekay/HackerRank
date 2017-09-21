dictionary = {}
n = int(raw_input())

for i in range(n):
    word = raw_input()
    if word not in dictionary:
        dictionary.update({word:1})
    else:
        val = dictionary.get(word)
        dictionary.update({word:val + 1})

itera = 0
m =int(raw_input())
while itera < m:
    query = raw_input()
    temp = dictionary.get(query)
    if temp ==  None:
        print 0
    else:
        print temp
    itera = itera + 1
