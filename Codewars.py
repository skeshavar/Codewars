def persistence(n):
    main = []
    count = 0
    if n / 10 > 0:
        start = True
    else:
        return count
    while start == True:
        count += 1
        for i in range(0,len(str(n))):
                main.append(n % 10)
                n = n / 10
        if len(main) > 1:
                prod = 1
                for i in main:
                    prod = prod * i
                if len(str(prod)) > 1:
                    n = prod
                    main = []
                    continue
                elif len(str(prod)) == 1:
                    start = False
    return count












persistence(14)