

array = ["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]

print sorted(array, key=lambda x: x==0 and type(x) is not bool) 
