score = list(map(int, (input().split(":"))))
first_team = score[0]
second_team = score[1]
if first_team < second_team:
    print(2)
elif first_team > second_team:
    print(1)
elif first_team == second_team:
    print(0)