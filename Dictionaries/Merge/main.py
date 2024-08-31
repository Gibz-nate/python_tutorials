def merge(dict1, dict2):
    ndic = {}
    for kv in dict1:
        ndic[kv] = dict1[kv]
    for kv in dict2:
        ndic[kv] = dict2[kv]
    return ndic        




def total_score(score_dict):
    total_score = 0
    for kv in score_dict:
        total_score += score_dict[kv]

    return total_score    

