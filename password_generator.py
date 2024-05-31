import streamlit as st
import random
import string

# Function to generate a random password
def generate_password(length, include_digits, include_special):
    characters = string.ascii_letters  # Include both uppercase and lowercase letters
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Streamlit app
def main():
    st.title("Simple Password Generator")

    # Input fields
    length = st.slider("Password Length", min_value=6, max_value=24, value=12)
    include_digits = st.checkbox("Include Digits")
    include_special = st.checkbox("Include Special Characters")

    # Generate password button
    if st.button("Generate Password"):
        password = generate_password(length, include_digits, include_special)
        st.success(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
