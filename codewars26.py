m = '4884'
count = 0
while count >= 0:
    if m[::1] != m[::-1]:
        m = str(int(m[::1]) + int(m[::-1]))
        count += 1
    else:
        print count
        break
        count = -1
    