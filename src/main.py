"""Password Generator - Main Entry Point.

This script demonstrates basic usage of the Password utility class by
generating and displaying different types of secure tokens.

Author: https://github.com/Taha-26
"""

from utils.Password import Password


def main():
    """Execute sample generations for PIN codes, character passwords, and passphrases."""
    print(Password.pin_code(10))
    print(Password.random_char(10, has_digit=True, has_symbol=True))
    print(Password.random_word(10, capitalize=True))


if __name__ == "__main__":
    main()
