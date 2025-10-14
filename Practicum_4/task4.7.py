score = list(map(int, (input().split())))
Kirill = score[0]
Arina = score[1]
Sergey = score[2]
if Kirill > Arina and Kirill > Sergey:
    print(Kirill)
elif Arina > Kirill and Arina > Sergey:
    print(Arina)
elif Sergey > Kirill and Sergey > Arina:
    print(Sergey)