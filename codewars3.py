n = "1 2 2"
n = n.split(" ")
s = ""
m = []

for i in n:
    m.append(int(i))

even = [x for x in m if x % 2 == 0]
odd = [x for x in m if x % 3 == 0]
for index, i in enumerate(m):
    if len(even) < len(odd) and i % 2 == 0:
        print index+1
        break
    elif len(odd) < len(even) and i % 2 != 0:
        print index+1
        break
        


        
    
