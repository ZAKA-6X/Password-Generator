# Password-Generator

This Python code generates a random password of varying length within a specified range and ensures it meets certain criteria for strength. Here's a breakdown:

    Imports: The code imports the random module to facilitate random selection.

    Character Pool: A string named caracter is defined, containing a range of characters including uppercase letters, lowercase letters, digits, and special symbols.

    Password Length: Randomly selects a password length between 8 and 23 characters.

    Password Generation: Using a while loop, it generates a password by randomly selecting characters from the caracter string until the password reaches the desired length.

    Password Strength Check: After generating a password, it checks if the password meets certain criteria for strength:
        Length: The password must be longer than 8 characters.
        Presence of Uppercase, Lowercase, and Numeric characters: It checks if the password contains at least one uppercase letter, one lowercase letter, and one numeric digit.

    Output: If the password meets all the criteria, it prints "Password is strong" and sets test to True, exiting the loop. Otherwise, it prints "password is weak" and continues the loop until a strong password is generated.

    Final Output: Once a strong password is generated, it prints the generated password.

This code ensures that the generated password is sufficiently strong by including a mix of character types and meeting a minimum length requirement.
