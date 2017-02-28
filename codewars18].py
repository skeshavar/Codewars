from math import sqrt
def gap(g, m, n):
    retn = []
    check = 0
    check_old = 0
    for i in range(m,n+1):
        square = int(round(sqrt(i)))
        print square
        if all(i%j!=0 for j in range(2,square)):
            check = i
            print check_old,check
            if check - check_old == g:
                    retn.append(check_old)
                    retn.append(check)
                    return retn
            else:
                check_old = i
            
                
    
    

    return None

print gap(10,300,400)