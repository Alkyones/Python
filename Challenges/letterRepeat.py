def letterRepeat(string):
    list_string = list(string)
    repeated = False
    for i in range(len(list_string)-1):
        if list_string[i] == list_string[i+1]:
            repeated = True
            return repeated
    return repeated
        





print(letterRepeat("a"))
print(letterRepeat("aa"))
print(letterRepeat("aadas dsakdkaskda"))