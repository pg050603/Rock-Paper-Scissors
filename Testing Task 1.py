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

i = 1;
while x == False
    microbit.display.show(ROCK)
microbit.display.sl
microbit.sleep

while not microbit.button_a.was_pressed():
    if microbit.button_b_was_pressed():
        i = i + 1

# Imports go at the top
import microbit

while True:
    if microbit.button_a.was_pressed():
        microbit.sleep(5000)
        p = (microbit.button_a.get_presses() % 3) - 1
        microbit.display.show(options[p])
    else:
        microbit.display.show(options[i])

    microbit.sleep(1000)

i = 2

Cycles = microbit.button_b.get_presses()
microbit.display.show(Cycles)

if microbit.button_a.was_pressed():
    microbit.display.show(8)
    microbit.sleep(1000)
    microbit.display.clear()




