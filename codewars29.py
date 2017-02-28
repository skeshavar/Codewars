def seperate_liquids(mm):
    if mm == []:
        return mm
    den = {"H": 1.36, "W" : 1.00, "A" : 0.87, "O" : 0.80}
    print sorted(den)
    k = ["H","W","A","O"]
    m = [ x for y in mm for x in y]
    n = sorted(m, key=den.get)

    def split_list(alist, wanted_parts=1):
        length = len(alist)
        return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
                for i in range(wanted_parts) ]


    return split_list(n, wanted_parts=len(mm))
    
print seperate_liquids([])