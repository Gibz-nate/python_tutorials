def calculate_experience_points(level):
    xp = 0
    total_xp = 0
    for i in range(1, level):
        if i == 1:
            xp = -5
        xp += 5
        xp1 = [xp]
        for i in xp1:
            total_xp += i
    result = total_xp + (level - 1) * 5
    return result

