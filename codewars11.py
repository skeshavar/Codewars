def scramble(s1,s2):
    s1= list(s1)
    s2= list(s2)
    s3 = []
    for i in s2:
        for index, j in enumerate(s1):
            if i == j:
                s3.append(i)
                s1[index] = ""
                break

    if s3 == s2:
        return True
    else:
        return False
        


print scramble('scriptjavx','javascript')