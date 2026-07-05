<img src="assets/banner.png">

---

# Password Generator

A secure password generator built in Python using the standard `secrets` module. This tool allows you to easily generate numeric PINs, complex character-based passwords, and highly secure, readable passphrases.

Author: [M.A Mohammadi](https://github.com/Taha-26)

---

## 🚀 Features

* **Secure PIN Generation:** Create numeric-only PIN codes of any length.
* **Customizable Alpha-Numeric Passwords:** Generate passwords with configurable options to include or exclude digits and special symbols (`string.punctuation`).
* **Memorable Passphrases:** Create word-based passphrases from a custom word list with adjustable separators and capitalization.
* **Cryptographically Secure:** Utilizes Python's `secrets` module (instead of `random`) to ensure tokens are secure enough for passwords and account recovery.

---

## 📂 Project Structure

```text
├── data/
│   └── words.txt          # Add your dictionary here 
├── utils/
│   ├── __init__.py
│   └── Password.py        # Core password generation logic
└── main.py                # Main entry point and demo script
```
---
## 🛠️ Getting Started
### Prerequisites
- Python 3.8 or higher is recommended.

### Setup & Usage
1. Clone the repository:
    ```shell
    git clone [https://github.com/Taha-26/Password-Generator.git](https://github.com/Taha-26/Password-Generator.git);cd Password-Generator
    ```
2. Prepare the Word List:
Make sure you have a data folder in the root directory containing a words.txt file. Add some words to it (each word on a new line) so the passphrase generator functions correctly.

3. Run the Demo:
    Execute the main script to see the generator in action:
    ```shell
    python main.py
    ```
---
## 💻 Quick Code Example
You can easily import the Password class into your own modules:
```python
Python
from utils.Password import Password

# 1. Generate a 6-digit numeric PIN
pin = Password.pin_code(6)
print(f"PIN: {pin}")

# 2. Generate a 16-character strong password with numbers and symbols
secure_pwd = Password.random_char(16, has_digit=True, has_symbol=True)
print(f"Password: {secure_pwd}")

# 3. Generate a 4-word memorable passphrase
passphrase = Password.random_word(4, separator="_", capitalize=True)
print(f"Passphrase: {passphrase}")
```