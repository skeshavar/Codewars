def isSolved(m):
    def xory(m):
        for i in m:
            if all(j==1 for j in i):
                return 1
            elif all(j==2 for j in i):
                return 2
            else:
                continue
    count  = 0
    new = []
    main = []
    if type(xory(m)) == int:
        return xory(m)
    while count < 3:
        for i in m:
            new.append(i[count])
        main.append(new)
        new = []
        count += 1
    if type(xory(main)) == int:
        return xory(main)
    for i in range(0,3):
        new.append(m[i][i])
    main = []
    main.append(new)
    if type(xory(main)) == int:
        return xory(main)
    else:
        new = []
        main = []
        m = m[::-1]
        for i in range(0,3):
            new.append(m[i][i])
        main = []
        main.append(new)
        if type(xory(main)) == int:
            return xory(main)
    for i in m:
        if 0 in i:
            return -1
    return 0
    
    