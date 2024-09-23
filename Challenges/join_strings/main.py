def join_strings(strings):
    jn = ""
    for str in strings:
        if jn != "":
            jn += ","
        jn += str
    return jn
        
        
