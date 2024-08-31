def split_players_into_teams(players):
    even_team = []
    odd_team = []
    for player in range(0, len(players)):
        if player % 2 == 0:
            even_team.append(players[player])
        else:
            odd_team.append(players[player]) 
    return even_team, odd_team            