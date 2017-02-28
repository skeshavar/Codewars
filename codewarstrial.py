def isPP(num):
    import math 
    square = int(math.sqrt(num))
    
    for i in range(2,square+1):
        new = (math.log(num)/math.log(i))
        if abs(new - round(new)) > 0 and abs(new - round(new)) < 1 * 10 ** -10:
            if round(new) > 1.0:
                return [i,int(round(new))] 
        if new % 1 == 1.0 or new % 1 == 0.0:
            if round(new)>1.0:
                return [i,int(round(new))]
                

print isPP()
