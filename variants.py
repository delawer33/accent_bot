def variants(word):
    vowels = 'уеыаоэяиюё'
    var_list = []
    for i in range(len(word)):
        if word[i] in vowels:
            var_list.append(word[:i]+word[i].upper()+word[i+1:])

    return var_list
