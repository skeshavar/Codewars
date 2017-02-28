
def primeFactors(num):
    count = 2
    main = []
    while count > 0:
        if num == 1:
            count == 0
            break
        elif count == 2:
            if num % count == 0:
                num = num / count
                main.append(count)
            else:
                count += 1
    
        elif count % 2 != 0:
            if num % count == 0:
                num = num / count
                main.append(count)
            else:
                count += 1
        else:
            count += 1
    m = sorted(set(main))

    strng = ""
    for i in m:
        if main.count(i) == 1:
            strng += "("+str(i)+")"
        else:
            strng += "("+str(i)+"**"+ str(main.count(i))+")"
    
    return strng
    
print primeFactors(3456)