direc = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
start = True
count = 0
while count < len(direc):
        if count == len(direc) - 1 :
            start == False
            break
            
        elif (direc[count] == "NORTH" and direc[count+1] == "SOUTH") or (direc[count] == "SOUTH" and direc[count+1] == "NORTH") :
            direc.pop(count)
            direc.pop(count)
            count = 0
            print "Found"
            print direc
            
        elif (direc[count] == "EAST" and direc[count+1] == "WEST") or (direc[count] == "WEST" and direc[count+1] == "EAST"):
            direc.pop(count)
            direc.pop(count)
            count = 0
            print "Found1"
            print direc
        
        else:
            count += 1
           
        
