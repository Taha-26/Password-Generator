import secrets
import string
from pathlib import Path
from typing import List


class Password:
    LETTERS = string.ascii_letters
    DIGITS = string.digits
    SYMBOLS = string.punctuation
    WORDS = []

    @staticmethod
    def check_len(max_len: int) -> str:
        if max_len < 1:
            raise ValueError("Length must be at least 1.")
        return ""

    @staticmethod
    def fill_words() -> List[str]:

        current_file = Path(__file__).resolve()

        project_root = current_file.parent.parent.parent
        file_path = project_root / "data" / "words.txt"

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"Error: file not found in {file_path}")
            return []

    @classmethod
    def pin_code(cls, max_len: int) -> str:

        cls.check_len(max_len)

        return "".join([secrets.choice(cls.DIGITS) for _ in range(max_len)])

    @classmethod
    def random_char(
        cls, max_len: int, has_digit: bool = False, has_symbol: bool = False
    ) -> str:

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
        cls.check_len(max_len)

        if not cls.WORDS:
            cls.WORDS = cls.fill_words()

        return separator.join([
            secrets.choice(cls.WORDS).capitalize()
            if capitalize
            else secrets.choice(cls.WORDS)
            for _ in range(max_len)
        ])
