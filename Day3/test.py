"""
Unit tests for the Palindrome Checker module using pytest.
"""

import pytest
from palindrome import is_palindrome, is_palindrome_number


class TestIsPalindrome:
    """Test suite for the is_palindrome string function."""

    def test_empty_string(self):
        """An empty string is trivially a palindrome."""
        assert is_palindrome("") is True

    @pytest.mark.parametrize("char", ["a", "Z", "9", "!", " "])
    def test_single_characters(self, char):
        """Any single character is a palindrome."""
        assert is_palindrome(char) is True

    @pytest.mark.parametrize(
        "word",
        [
            "racecar",
            "noon",
            "radar",
            "level",
            "deified",
            "rotator",
            "kayak",
            "reviver",
        ],
    )
    def test_valid_word_palindromes(self, word):
        """Standard odd and even length word palindromes."""
        assert is_palindrome(word) is True

    @pytest.mark.parametrize(
        "word",
        [
            "hello",
            "world",
            "python",
            "palindrome",
            "github",
            "testing",
        ],
    )
    def test_non_palindromes(self, word):
        """Strings that are not palindromes."""
        assert is_palindrome(word) is False

    @pytest.mark.parametrize(
        "phrase",
        [
            "A man, a plan, a canal: Panama!",
            "Was it a car or a cat I saw?",
            "No 'x' in Nixon",
            "Never odd or even",
            "Do geese see God?",
            "Eva, can I see bees in a cave?",
            "Madam, in Eden, I'm Adam",
        ],
    )
    def test_phrases_with_punctuation_and_spaces(self, phrase):
        """Phrases with spaces and punctuation should be recognized as palindromes by default."""
        assert is_palindrome(phrase) is True

    @pytest.mark.parametrize(
        "word, expected",
        [
            ("Racecar", False),
            ("Madam", False),
            ("Noon", False),
            ("racecar", True),
            ("noon", True),
        ],
    )
    def test_case_sensitivity_enabled(self, word, expected):
        """When ignore_case=False, case differences must be respected."""
        assert is_palindrome(word, ignore_case=False) is expected

    @pytest.mark.parametrize(
        "text, expected",
        [
            ("race car", False),
            ("madam, i'm adam", False),
            ("racecar", True),
            ("noon", True),
        ],
    )
    def test_punctuation_preserved_when_disabled(self, text, expected):
        """When ignore_punctuation=False, spaces and punctuation are not stripped."""
        assert is_palindrome(text, ignore_punctuation=False) is expected

    @pytest.mark.parametrize(
        "text, expected",
        [
            ("racecar", True),
            ("Racecar", False),
            ("race car", False),
            ("noon", True),
            ("Noon", False),
        ],
    )
    def test_strict_mode(self, text, expected):
        """Strict check with both ignore_case=False and ignore_punctuation=False."""
        assert (
            is_palindrome(text, ignore_case=False, ignore_punctuation=False)
            is expected
        )

    @pytest.mark.parametrize(
        "text, expected",
        [
            ("12321", True),
            ("1a2b2a1", True),
            ("12345", False),
            ("Able was I ere I saw Elba", True),
        ],
    )
    def test_alphanumeric_mix(self, text, expected):
        """Strings containing combinations of digits and letters."""
        assert is_palindrome(text) is expected

    @pytest.mark.parametrize("invalid_input", [12321, None, ["r", "a", "c", "e", "c", "a", "r"], 3.14, {}])
    def test_invalid_type_raises_type_error(self, invalid_input):
        """Non-string inputs must raise TypeError."""
        with pytest.raises(TypeError, match="Expected string input"):
            is_palindrome(invalid_input)  # type: ignore


class TestIsPalindromeNumber:
    """Test suite for the is_palindrome_number mathematical function."""

    @pytest.mark.parametrize("digit", list(range(10)))
    def test_single_digits(self, digit):
        """All single digits 0-9 are palindromes."""
        assert is_palindrome_number(digit) is True

    @pytest.mark.parametrize(
        "number",
        [
            121,
            1221,
            12321,
            1234321,
            12344321,
            9999999,
        ],
    )
    def test_positive_palindromes(self, number):
        """Even and odd length palindrome integers."""
        assert is_palindrome_number(number) is True

    @pytest.mark.parametrize(
        "number",
        [
            123,
            10,
            100,
            123456,
            1000021,
        ],
    )
    def test_positive_non_palindromes(self, number):
        """Non-palindrome integers."""
        assert is_palindrome_number(number) is False

    @pytest.mark.parametrize(
        "negative_number",
        [
            -1,
            -121,
            -1221,
            -12321,
        ],
    )
    def test_negative_numbers(self, negative_number):
        """Negative numbers cannot be palindromes due to minus sign."""
        assert is_palindrome_number(negative_number) is False

    @pytest.mark.parametrize("invalid_input", ["121", 12.21, None, [1, 2, 1]])
    def test_invalid_type_raises_type_error(self, invalid_input):
        """Non-integer inputs must raise TypeError."""
        with pytest.raises(TypeError, match="Expected int input"):
            is_palindrome_number(invalid_input)  # type: ignore


if __name__ == "__main__":
    pytest.main(["-v", __file__])
