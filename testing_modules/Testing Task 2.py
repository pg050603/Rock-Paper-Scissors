import random

opponent_id = random.randint(0, 99)
str_id = bytes(str(opponent_id), 'UTF-8')

print(str_id)