"""Password Generator - Main Entry Point.

Author: https://github.com/Taha-26
"""

from utils.Password import Password


def main():

    print(Password.pin_code(10))
    print(Password.random_char(10, has_digit=True, has_symbol=True))
    print(Password.random_word(10, capitalize=True))


if __name__ == "__main__":
    main()
