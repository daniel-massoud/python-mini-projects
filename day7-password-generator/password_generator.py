import random
import string


def get_user_options():
    """Ask the user for password preferences and return them."""
    print("\n🔐 Password Generator - Day 7")

    while True:
        try:
            length = int(input("Enter password length (minimum 6): "))
            if length < 6:
                print("❗ Password must be at least 6 characters.")
                continue
            break
        except ValueError:
            print("❗ Please enter a valid number.")

    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    return length, include_uppercase, include_numbers, include_symbols


def generate_password(length, include_uppercase, include_numbers, include_symbols):
    """Generate a password based on user preferences."""

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_uppercase else ""
    digits = string.digits if include_numbers else ""
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?" if include_symbols else ""

    all_chars = lower + upper + digits + symbols

    if not all_chars:
        raise ValueError("No characters available for password generation!")

    # Guarantee at least one character from each selected set
    password = []

    if include_uppercase:
        password.append(random.choice(upper))
    if include_numbers:
        password.append(random.choice(digits))
    if include_symbols:
        password.append(random.choice(symbols))

    # Fill the rest
    while len(password) < length:
        password.append(random.choice(all_chars))

    # Shuffle the final password
    random.shuffle(password)
    return ''.join(password)


def main():
    while True:
        length, include_uppercase, include_numbers, include_symbols = get_user_options()

        password = generate_password(length, include_uppercase, include_numbers, include_symbols)
        print("\n✅ Your generated password:")
        print("👉", password)

        again = input("\nGenerate another password? (y/n): ").lower()
        if again != 'y':
            print("\nThanks for using the password generator! 🔒")
            break


if __name__ == "__main__":
    main()
