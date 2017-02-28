def list_squared(m,n):
    from math import sqrt
    final = []
    for x in range(m,n):
        i = 1
        sum = 0
        large = []
        for i in xrange(1, int(sqrt(x) + 1)):
            if x % i == 0:
                large.append(int(i))
                if i*i != x:
                    large.append(int(x / i))
        for i in large:
            sum += i**2
        if sqrt(sum)%1 <= 0.0:
            final.append([x,sum])
        
    return final
    
        
    

print list_squared(42,250)