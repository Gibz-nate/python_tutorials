def get_champion_slices(champions):
    s1 = champions[2:]
    s2 = champions[:-3+1]
    s3 = champions[::2]
    return s1, s2, s3
