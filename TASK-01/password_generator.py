# Purpose: Generate a random password of the desired length
# Input: Desired password length
# Output: Random password of provided length
# Author: Sneh Kumar

import random
import string


# Generate a random password of the desired length
def gen_password(length):
    characters = (
        string.digits + string.punctuation + string.hexdigits + string.ascii_letters
    )
    password = "".join(random.choice(characters) for _ in range(length))
    return password


# For 1st 2nd 3rd .. Formatting
num_suffix = (
    lambda n: "th"
    if 10 <= n % 100 <= 20
    else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
)


def main():
    try:
        # Get desired password length from the user
        password_length = int(input("Enter the desired length of the password: "))
        num_passwords = int(input("Enter the number of passwords to generate: "))

        # Check if the length is valid
        if password_length <= 0:
            print("Please enter a valid password length.")
            return

        # Generate the passwords
        for _ in range(num_passwords):
            password = gen_password(password_length)
            print(f"{_ + 1}{num_suffix(_ + 1)}", "Password: ", password)

    except ValueError:
        print("Please enter a valid integer for the password length.")


if __name__ == "__main__":
    main()
