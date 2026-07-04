"""Password Generator - Core password generator

    This module provides the Password class which utilizes the cryptographically secure
'secrets' module to generate PINs, character-based passwords, and passphrases.

Author: https://github.com/Taha-26"""

import secrets
import string
from pathlib import Path
from typing import List


class Password:
    """A class containing static and class methods to generate secure passwords."""

    LETTERS = string.ascii_letters
    DIGITS = string.digits
    SYMBOLS = string.punctuation
    WORDS = []

    @staticmethod
    def check_len(max_len: int) -> str:
        """Validate that the requested password length is acceptable.

        :param max_len: The requested length of the password or PIN.

        :returns: An empty string if validation passes.

        :raises ValueError: If max_len is less than 1.
        """

        if max_len < 1:
            raise ValueError("Length must be at least 1.")
        return ""

    @staticmethod
    def fill_words() -> List[str]:
        """Load a list of words from an external text file for passphrase generation.
        Resolves the file path relative to this script's location.

        :returns: A list of stripped, non-empty words from the file.
        """
        current_file = Path(__file__).resolve()

        project_root = current_file.parent.parent.parent
        file_path = project_root / "data" / "words.txt"

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            raise FileNotFoundError(f"Error: file not found in {file_path}")
            return []

    @classmethod
    def pin_code(cls, max_len: int) -> str:
        """Generate a secure numeric PIN code.

        :param max_len: The number of digits for the PIN.

        :returns: The generated numeric PIN string.
        """
        cls.check_len(max_len)

        return "".join([secrets.choice(cls.DIGITS) for _ in range(max_len)])

    @classmethod
    def random_char(
        cls, max_len: int, has_digit: bool = False, has_symbol: bool = False
    ) -> str:
        """Generate a random character-based password.

        Allows customization to include digits and special symbols alongside letters.

        :param max_len: The length of the generated password.
        :param has_digit: Flag to include numbers (0-9), defaults to False.
        :param has_symbol: Flag to include special characters/symbols, defaults to False.

        :returns: The generated alphanumeric/symbolic password.
        """
        cls.check_len(max_len)
        pool = cls.LETTERS

        if has_digit:
            pool += cls.DIGITS
        if has_symbol:
            pool += cls.SYMBOLS

        return "".join([secrets.choice(pool) for _ in range(max_len)])

    @classmethod
    def random_word(
        cls, max_len: int, separator: str = "-", capitalize: bool = False
    ) -> str:
        """Generate a passphrase consisting of multiple random words.

        :param max_len: The number of words to include in the passphrase.
        :param separator: The string used to join the words, defaults to "-".
        :param capitalize: If True, capitalizes the first letter of each word, defaults to False.

        :returns: The generated word-based passphrase.
        """
        cls.check_len(max_len)

        # loading pattern to populate the cache only when needed
        if not cls.WORDS:
            cls.WORDS = cls.fill_words()

        return separator.join([
            secrets.choice(cls.WORDS).capitalize()
            if capitalize
            else secrets.choice(cls.WORDS)
            for _ in range(max_len)
        ])
