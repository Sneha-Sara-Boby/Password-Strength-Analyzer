"""
Password Strength Analyzer
--------------------------
A beginner-friendly Python program that checks the strength of a password.

Features:
- Minimum length check
- Uppercase letter check
- Lowercase letter check
- Number check
- Special character check
- Password strength scoring
- Clear feedback on missing requirements
- Uses regular expressions (regex)
- Organised into functions
- Handles invalid input
- Follows PEP 8 coding standards
"""

import re


def get_password():
    """
    Ask the user to enter a password.

    Returns:
        str: A valid password entered by the user.
    """
    while True:
        password = input("Enter your password: ")

        # Check if the input is empty
        if not password.strip():
            print("Error: Password cannot be empty.\n")
            continue

        return password


def check_password(password):
    """
    Check password against security requirements.

    Args:
        password (str): Password entered by the user.

    Returns:
        tuple:
            score (int): Password score.
            missing (list): Missing requirements.
    """

    score = 0
    missing = []

    # Check minimum length
    if len(password) >= 8:
        score += 1
    else:
        missing.append("Minimum 8 characters")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        missing.append("At least one uppercase letter")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        missing.append("At least one lowercase letter")

    # Check for numbers
    if re.search(r"\d", password):
        score += 1
    else:
        missing.append("At least one number")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=/\\[\]]", password):
        score += 1
    else:
        missing.append("At least one special character")

    return score, missing


def determine_strength(score):
    """
    Determine password strength based on score.

    Args:
        score (int): Password score.

    Returns:
        str: Password strength.
    """

    if score <= 2:
        return "Weak"
    if score == 3:
        return "Medium"
    if score == 4:
        return "Strong"
    return "Very Strong"


def display_results(score, strength, missing):
    """
    Display password analysis results.

    Args:
        score (int): Password score.
        strength (str): Password strength.
        missing (list): Missing requirements.
    """

    print("\n========== Password Analysis ==========")
    print(f"Strength Score : {score}/5")
    print(f"Password Rating: {strength}")

    if missing:
        print("\nMissing Requirements:")
        for item in missing:
            print(f"- {item}")
    else:
        print("\nExcellent! Your password meets all security requirements.")

    print("=======================================")


def main():
    """
    Main program execution.
    """

    print("Password Strength Analyzer")
    print("-" * 30)

    password = get_password()

    score, missing = check_password(password)

    strength = determine_strength(score)

    display_results(score, strength, missing)


# Run the program
if __name__ == "__main__":
    main()