"""
An example of the strategy pattern.
"""
import abc


class CheckStrategy(abc.ABC):
    """
    Abstract base class for the algorithm
    """

    @abc.abstractmethod
    def check(self, s: str) -> bool:
        """
        Checks the incoming string
        """

class All(CheckStrategy):
    """
    Passes with all strings
    """

    def check(self, s: str) -> bool:
        """
        Returns True for all strings
        """
        return True


class StartsWithT(CheckStrategy):
    """
    Passes with strings starting with the character 't'
    """

    def check(self, s: str) -> bool:
        """
        Returns True for any strings starting with the character 't'
        """
        if len(s) == 0:
            return False

        return s.startswith('t')


class LongerThan5(CheckStrategy):
    """
    Passes with strings of length greater than 5
    """

    def check(self, s: str) -> bool:
        """
        Returns True for strings of length greater than 5
        """
        return len(s) > 5


class Palindrome(CheckStrategy):
    """
    Passes with strings that are palindromes
    """

    def check(self, s: str) -> bool:
        """
        Returns True for strings that are palindromes
        """
        return s == s[::-1]


class Context:
    pass