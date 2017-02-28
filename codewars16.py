def sum_pairs(l1, s):
    sub = []
    sub_1 = []
    main = []
    main_1 = []
    count = 0
    count_next = 0
    while count < len(l1)-1:
    
        count_next += 1
        if l1[count] + l1[count_next] == s:
            sub_1.append(l1[count]) 
            sub_1.append(l1[count_next])
            sub.append(count)
            sub.append(count_next)
            main.append(sub)
            main_1.append(sub_1)
            sub = []
            sub_1= []
        if count_next == len(l1)-1:
            count_next = count+1
            count += 1
    
    if len(main) == 0:
        return None
    elif len(main) == 1:
        return main_1[0]
    else:
        for index, i in enumerate(main):
            if index == len(main)-1:
                break
            if main[index][0] < main[index+1][0] and main[index][1] < main[index+1][1]:
                return main_1[index]
            if main[index+1][0] > main[index][0] and main[index+1][1] < main[index][1]:
                return main_1[index+1]

l8= [5, 9, 13, -3]

print sum_pairs(l8, 10)
            

    
    
    