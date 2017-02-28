

def productFib(prod):
    main = [1,1]
    strng = []
    count = 0
    while count >= 0:
        new = main[count]+main[count+1]
        if main[count]*main[count+1] == prod:
            strng.append(main[count])
            strng.append(main[count+1])
            strng.append(True)
            return strng
            break
        elif main[count]*main[count+1] > prod:
            strng.append(main[count])
            strng.append(main[count+1])
            strng.append(False)
            count = -1
            return strng
        else:
            main.append(new)
            count += 1
            
print productFib(5895)
