def isPP(num):
    import math 
    square = int(math.sqrt(num))
    for i in range(2,square+50):
        new = (math.log(num)/math.log(i))
        if new % 1 > 0:
            continue
        else:
            if int(new)>1:
                return [i,int(new)]