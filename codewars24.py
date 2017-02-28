num = 119989884756 
num_new = list(str(num))
if min(num_new) == num_new[0]:
    repl = num_new.pop(num_new.index(min(num_new[1::])))
    
    num_new[2::] = num_new[1::]
    
    num_new[1] = repl
else:
    repl = num_new.pop(num_new.index(min(num_new)))
    ind = num_new.index(min(num_new))
    num_new[1::] = num_new[0::]
    num_new[0] = repl
    
    
num_new = "".join(num_new)
print int(num_new)