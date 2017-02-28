def first_non_repeating_letter(string):
    string_new  = string.lower()
    for index, i in enumerate(string_new):
        if string_new.count(i) == 1:
            return string[index]


print first_non_repeating_letter('STresS')