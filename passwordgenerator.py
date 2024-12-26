'''
TASK :- PASSWORD GENERATOR:
----    -------------------

--> A password generator is a useful tool that generates strong and random passwords for users. This project aims to create a password generator application using Python, allowing users to specify the length and complexity of the password.

User Input: Prompt the user to specify the desired length of the password.
---- -----

Generate Password: Use a combination of random characters to generate a password of the specified length.
-------- --------

Display the Password: Print the generated password on the screen.
------- --- --------
'''

from random import choice
from string import printable

class PasswordGenerator:
    """
    A class to generate random passwords of a specified length.

    Attributes:
    -----------
    length : int
        The length of the password to be generated.
    characters : str
        The set of characters to be used in the password.

    Methods:
    --------
    generate_password():
        Generates a random password of the specified length.
    __str__():
        Returns a string representation of the generated password.
    """

    def __init__(self, length: int) -> None:
        """
        Initializes the PasswordGenerator with the specified length and character set.

        Parameters:
        -----------
        length : int
            The length of the password to be generated.
        """
        self.length = length
        self.characters = printable.strip()  # Remove whitespace characters

    def generate_password(self) -> str:
        """
        Generates a random password of the specified length.

        Returns:
        --------
        str
            The generated password.
        """
        self.password = "".join(choice(self.characters) for _ in range(self.length))
        return self.password

    def __str__(self) -> str:
        """
        Returns a string representation of the generated password.

        Returns:
        --------
        str
            A string representation of the generated password.
        """
        return f"Generated Password:{self.generate_password()}"

def get_user_input() -> int:
    """
    Prompts the user to input the desired length of the password and validates the input.

    Returns:
    --------
    int
        The validated length of the password.
    """
    while True:
        try:
            length = int(input("Enter the length of the password (between 1 and 100): "))
            if 1 <= length <= 100:
                return length
            else:
                print("-"*20)
                print("Password length must be between 1 and 100. ⚠️")
                print("-"*20)
        except ValueError:
            print("-"*20)
            print("Please enter a valid number. 🔢")
            print("-"*20)

def main():
    """
    The main function to run the password generator application.

    Prompts the user to input the desired length of the password, validates the input,
    creates an instance of PasswordGenerator with the specified length, and displays the generated password.
    """
    print("-" * 20)
    print("Password Generator 🔒")
    print("-" * 20)
    print("Generate a strong and random password. 😎")
    print("-" * 20)
    print()
    length = get_user_input()
    print("-" * length)
    password_generator = PasswordGenerator(length)
    print(password_generator)
    print("-" * length)
    print("Your password is ready! ✅")

if __name__ == '__main__':
    main()
