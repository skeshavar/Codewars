def gap(g, m, n):
    retn = []
    check = 0
    check_old = 0
    for i in range(m,n+1):
        if all(i%j!=0 for j in range(2,i)):
            check = i
            print check_old,check
            if check - check_old == g:
                    retn.append(check)
                    retn.append(check_old)
                    return retn
            else:
                check_old = i
            
                
    
    

    return None

print gap(10,300,400)