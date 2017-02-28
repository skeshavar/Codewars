def duplicate_count(test):
    test = test.lower()
    chk = []
    for index, i in enumerate(test):
        if i in test[index+1:len(test)] and i not in chk:
            chk.append(i)
    return len(chk)

print duplicate_count("abcdeaB")