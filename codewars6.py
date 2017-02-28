def find_even_index(lst):
    for index, i in enumerate(lst):
        if sum(lst[0:index]) == sum(lst[index+1:len(lst)]):
            return index
    return -1
   
print find_even_index([1,2,3,2,1])
    
   


    