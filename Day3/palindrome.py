"""
Palindrome Checker Module.

Provides functions to check whether strings or numbers are palindromes,
with configurable options for case sensitivity and whitespace/punctuation filtering.
"""

import re


def is_palindrome(
    text: str,
    ignore_case: bool = True,
    ignore_punctuation: bool = True,
) -> bool:
    """
    Check if a given string is a palindrome.

    A palindrome is a word, phrase, number, or other sequence of characters
    that reads the same forward and backward.

    Args:
        text (str): The string to check.
        ignore_case (bool): If True, case differences are ignored (default: True).
        ignore_punctuation (bool): If True, non-alphanumeric characters (spaces,
            punctuation, symbols) are ignored (default: True).

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected string input, got {type(text).__name__}")

    processed = text

    if ignore_punctuation:
        # Keep only alphanumeric characters (letters and numbers)
        processed = re.sub(r"[^A-Za-z0-9]", "", processed)

    if ignore_case:
        processed = processed.lower()

    return processed == processed[::-1]


def is_palindrome_number(n: int) -> bool:
    """
    Check if an integer is a palindrome without converting it to a string.

    Negative numbers are not palindromes due to the leading minus sign.

    Args:
        n (int): The integer to check.

    Returns:
        bool: True if the integer is a palindrome, False otherwise.

    Raises:
        TypeError: If the input is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError(f"Expected int input, got {type(n).__name__}")

    # Negative numbers and numbers ending with 0 (except 0 itself) cannot be palindromes
    if n < 0 or (n % 10 == 0 and n != 0):
        return False

    reversed_half = 0
    # Reverse the second half of the number
    while n > reversed_half:
        reversed_half = reversed_half * 10 + n % 10
        n //= 10

    # For even-digit numbers: n == reversed_half
    # For odd-digit numbers: n == reversed_half // 10 (discards middle digit)
    return n == reversed_half or n == reversed_half // 10


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        result = is_palindrome(query)
        print(f"'{query}' -> {'Palindrome' if result else 'Not a palindrome'}")
    else:
        sample_phrases = [
            "racecar",
            "A man, a plan, a canal: Panama",
            "Was it a car or a cat I saw?",
            "No 'x' in Nixon",
            "hello world",
        ]
        print("Palindrome Checker Examples:")
        for phrase in sample_phrases:
            status = "Palindrome" if is_palindrome(phrase) else "Not a palindrome"
            print(f"  {phrase!r:35} => {status}")
