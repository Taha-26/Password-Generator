"""Password Generator - Main Entry Point.

This script manages the frontend web interface using Streamlit, allowing users
to interactively generate cryptographically secure PINs, passwords, and passphrases.

Author: https://github.com/AmiinMohammadi
"""

import streamlit as st

# Import the core logic from the utility module
from utils.Password import Password


def main():
    """Main function that builds the Streamlit UI and handles user inputs."""

    # Define the generation strategies available in the UI
    OPTIONS = ["PIN code", "Random characters", "Random words"]

    # App header
    st.title("Password Generator App")
    option = st.radio("Select Type:", OPTIONS)

    # Set up a slider for defining password/passphrase lengths (range: 4-20, default: 8)
    password_len = st.slider("Length of password:", 4, 20, 8)

    # Branching logic based on the user's selected generator type
    if option == OPTIONS[0]:
        generated_password = Password.pin_code(password_len)

    elif option == OPTIONS[1]:
        generated_password = Password.random_char(
            password_len, has_digit=st.toggle("Number"), has_symbol=st.toggle("Symbol")
        )

    else:
        generated_password = Password.random_word(
            password_len,
            capitalize=st.toggle("Capitalize"),
            separator=st.text_input("Separator", value="-"),
        )

    # Execution trigger button
    if st.button("Generate :sparkles: "):
        # Visual indicator of successful completion
        st.success("Successful Generate.")
        # Render the final token in a secure, easy-to-copy text container
        st.code(generated_password, language="text")


if __name__ == "__main__":
    main()
