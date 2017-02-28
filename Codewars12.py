def format_duration(num):
    num1 = num
    time = {}
    quot = num/31536000
    if quot > 0:
        time['year'] = quot
        rem = num % 31536000
        num = rem
    else:
        num = num % 31536000
        time['year'] = 0
    quot_1 = num/86400
    if quot_1 > 0:
        time['day'] = quot_1
        rem_1 = num % 86400
        num = rem_1
    else:
        num = num % 86400
        time['day'] = 0
    quot_2 = num/3600
    if quot_2 > 0:
        time['hour'] = quot_2
        rem_2 = num % 3600
        num = rem_2
    else:
        num = num % 3600
        time['hour'] = 0
    quot_3 = num/60
    if quot_3 > 0:
        time['minute'] = quot_3
        rem_3 = num % 60
        num = rem_3
    else:
        num = num % 60
        time['minute'] = 0
    if num == 0:
        time['second'] = 0
    else:
        time['second'] = num
    
    read_lst_old = ['year','day','hour','minute','second']
    read_lst = []
    for i in read_lst_old:
        if time[i] != 0:
            read_lst.append(i)
    
    read_time = ""
    for index, key in enumerate(read_lst):
        if num1 > 0 and num1 < 60:
            if time['second'] == 1:
                    read_time += str(time['second']) + " "+ "second" 
            elif time['second'] > 1:
                    read_time += str(time['second']) + " "+ "seconds"
            return read_time

        elif num1 == 0:
            read_time += "now"
            return read_time

        elif index != len(read_lst)-1 and len(read_lst) > 1:
             if time[key] != 0 and time[key] == 1:
                 read_time += str(time[key]) + " "+ key + ", " 
             elif time[key] != 0 and time[key] > 1:
                 read_time += str(time[key]) + " "+ key + "s" + ", "
             else:
                 continue

        elif index == len(read_lst) - 1:
             if len(read_lst) == 1:
                 if time[key] != 0 and time[key] == 1:
                    read_time += str(time[key]) + " "+ key  
                 elif time[key] != 0 and time[key] > 1:
                    read_time += str(time[key]) + " "+ key + "s" 
             else:
                 s = list(read_time)
                 s.pop(len(s)-2)
                 
                 read_time = "".join(s)
                 if time[key] != 0 and time[key] == 1:
                    read_time += "and " + str(time[key]) + " "+ key  
                 elif time[key] != 0 and time[key] > 1:
                    read_time += "and " + str(time[key]) + " "+ key + "s"  
    s = list(read_time)
    if s[len(s)-1] == " ":
        s.pop(len(s)-1)
        read_time = "".join(s)
                
            
        return read_time
    else:
        read_time = "".join(s)
        return read_time
   
            
    
print format_duration(242354454)
     
    