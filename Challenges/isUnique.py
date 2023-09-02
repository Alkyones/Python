def has_unique_characters(keyword):
    list_keyword = list(keyword)
    set_keyword = set(list_keyword)
    
    return (len(list_keyword) == len(set_keyword))
    
print(has_unique_characters("abcdefg"))  # Output: True
print(has_unique_characters("hello"))    # Output: False
