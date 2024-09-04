def find_missing_ids(first_ids, second_ids):
    rmv = set()

    first = set(first_ids)
    second = set(second_ids)
    
    sub = first - second
    rmv.update(sub)

    fin = list(rmv)

    return fin
