print('Введите плей-лист папы (когда песни закончатся, введите пустую строку):')
father_playlist = []

while True:
    song = input()
    if song == "":
        break
    father_playlist.append(song)

mother_playlist = father_playlist[::-1]
print('\nПлейлист мамы:')
print('\n'.join(mother_playlist))