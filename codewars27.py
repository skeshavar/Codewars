def make_readable(num):   
    time = {}
    quot_1 = num/3600
    if quot_1 > 0:
        time['hour'] = quot_1
        rem_1 = num % 3600
        num = rem_1
    else:
        num = num % 3600
        time['hour'] = 00
    quot_2 = num/60
    if quot_2 > 0:
        time['minute'] = quot_2
        rem_2 = num % 60
        num = rem_2
    else:
        num = num % 60
        time['minute'] = 00
    if num == 0:
        time['second'] = 00
    else:
        time['second'] = num
    
    return '%02d:%02d:%02d' % (time['hour'],time['minute'],time['second'])
    
print make_readable(359999)
    