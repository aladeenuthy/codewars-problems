def is_isogram(string):
    is_a_isogram = True
    list_string = list(str(string).lower())
    for element in list_string:
        if list_string.count(element) > 1:
            is_a_isogram = False
            break
    return is_a_isogram