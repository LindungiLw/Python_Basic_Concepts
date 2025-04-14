def swap_first_last(team):
    if len(team) > 1:
        team[0], team[-1] = team[-1], team[0]
    return team

team = ['Ava', 'Eleanor', 'Clare', 'Sarah']
swapped_team = swap_first_last(team)

print(swapped_team)