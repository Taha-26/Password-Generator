<img src="assets/banner.png">

---

# Password Generator

A responsive web application built with Python and **Streamlit** that generates secure passwords, custom PINs, and memorable passphrases. It leverages Python's built-in `secrets` module to ensure all outputs are cryptographically sound and secure against predictability.

Author: [M.A Mohammadi](https://github.com/AmiinMohammadi)

---

## ✨ Features

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
└── app.py                 # Streamlit UI interface & entry point
```
---
## 🚀 Getting Started

### Prerequisites

Make sure you have Python installed on your system. You will need the `streamlit` package to run the graphical web interface.

### Installation
1. Clone the repository:
    ```shell
    git clone https://github.com/AmiinMohammadi/Password-Generator.git

    cd Password-Generator
    ```
2. Install dependencies:
    ```shell
    pip install streamlit=1.58.0
    ```
3. Provide a Wordlist File:

    Ensure you have a text file filled with newline-separated words located precisely under `data/words`.txt for the random passphrase feature to work correctly.

---

## 🛠️ How to Run

Launch the Streamlit server from your terminal inside the project directory:

```shell
streamlit run src/app.py
```
---
Once executed, a local browser window will open automatically at `http://localhost:8501`.
