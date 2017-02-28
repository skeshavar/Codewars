from collections import defaultdict
from sortedcontainers import SortedDict
dict = defaultdict(list)
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

m = []
s1 = 'looping is fun but dangerous'
s2 = "less dangerous than coding"
for i in alpha:
    add = ""
    for j in s1:
        if i == j:
            add += j
    dict[i].append(add) 
    add = ""
    for j in s2:
        if i == j:
            add += j
    dict[i].append(add)
dict = SortedDict(dict)
count1 = []
count2 = []
for i in dict:
    count1.append(len(dict[i][0]))
    count2.append(len(dict[i][1]))

max1 = max(count1)
max2 = max(count2)
if max1 > max2:
    maxi = max1
elif max2 > max1:
    maxi = max2
elif max1 == max2:
    maxi = max1
max_lst = range(2,maxi+1)
max_lst = max_lst[::-1]
final = ""

for n in max_lst:
    for i in dict:
        if len(dict[i][0]) == n and len(dict[i][0]) > len(dict[i][1]):
            final += "1:" + dict[i][0]+ "/"
    for i in dict:
        if len(dict[i][1]) == n and len(dict[i][1]) > len(dict[i][0]) :
                final += "2:" + dict[i][1]+ "/" 
    for i in dict:
        if  len(dict[i][0]) == n and len(dict[i][0]) == len(dict[i][1]):
                final += "=:" + dict[i][0]+ "/"

if final == "":
    print final
else:
    s = list(final)
    print s
    s.pop(len(s)-1)
    print s
    final = "".join(s)
    print final
    print maxi
print dict