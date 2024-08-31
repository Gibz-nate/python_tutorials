def get_most_common_enemy(enemies_dict):
    max_so_far = float("-inf")
    enemy_name = None

    for enemy, count in enemies_dict.items():
        if count > max_so_far:
            max_so_far = count
            enemy_name = enemy
    return enemy_name




        

    