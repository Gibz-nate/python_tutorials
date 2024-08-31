'''def reverse_array(items):
    
    return items[::-1]'''

#second method
def reverse_array(items):
    reversed = []
    for i in items:
        reversed.insert(0, i)
    return reversed    
    
