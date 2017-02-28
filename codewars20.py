big = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
n=10
count = 1
new = ""
while count <= n:
    if count == n:
        print big[0]
        break
    big.append(big[0])
    big.append(big[0])
    big.pop(0)
    count += 1
    

print big

    
    