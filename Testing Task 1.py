RPS = (b'R', b'P', b'S')
i = 0
play = None


while play is None:
    confirm_play = input(b"Do you want to play " + RPS[i] + b" ?")

    if confirm_play == 'Y':
        play = RPS[i]
    else:
        if i == 2:
            i = 0
        elif i != 2:
            i = i + 1

print(play)


