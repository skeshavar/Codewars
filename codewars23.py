def pig_it(text):
    add = 'ay'
    strng = text.split()
    for index, i in enumerate(strng):
        first = i[0]
        strng[index] = i[1::] + first + add
        
        
        
    return " ".join(strng)
    


        
print pig_it('This is my string')