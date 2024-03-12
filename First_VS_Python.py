import time

def print_delay(message, delay):
    for char in message:
        print(char, end = '')
        time.sleep(delay)
    print()


if __name__ == "__main__":

    message = "Shit, this message is written symbol-by-symbol. Damn, this is awesome!"
    delay = 0.04

    print_delay(message, delay)


    print_delay(message, 0.05)
    print_delay(message, 0.01)
