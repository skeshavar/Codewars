def square_digits(num):
    n = []
    m = ""
    for i in range(0, len(str(num))):
        rem = num % 10
        n.append(rem)
        num = num / 10
    n = n[::-1]
    
    for index, i in enumerate(n):
        n[index] = i ** 2
        
    for i in n:
        m += str(i)
    
    return m
    
square_digits(9119)
    
