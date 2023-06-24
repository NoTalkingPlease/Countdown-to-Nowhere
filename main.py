import random
import time

def countdown():
    countdown_number = random.randint(1, 10)

    while True:
        print(countdown_number)
        time.sleep(1)
        countdown_number -= 1

        if countdown_number <= 0:
            countdown_number = random.randint(1, 10)

countdown()
