#!/usr/bin/env python3.10

# Created by: Nicolas Riscalas
# Created on: May 2 2022
# display a colour wheel


def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)


def main():
    counter = 0
    counter2 = 0
    counter3 = 0
    for counter in range(256):
        for counter2 in range(256):
            for counter3 in range(25):
                print(
                    colored(
                        counter,
                        counter2,
                        counter3,
                        "rgb code = {},{},{}".format(counter, counter2, counter3),
                    )
                )


if __name__ == "__main__":
    main()
