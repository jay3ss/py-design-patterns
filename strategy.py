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
    def __init__(self, strategy=All(), callback=print) -> None:
        self._strategy = strategy
        self._callback = callback

    def change_strategy(self, strategy: CheckStrategy) -> None:
        """
        Changes the strategy used to filter files
        """
        self._strategy = strategy

    def filter(self, filename: str) -> None:
        """
        Filters out the text from a file using the given strategy
        """
        chars_to_strip = ':,.\n'
        # go through each word in the file and if the word passes the check,
        # then pass it to the callback
        with open(filename, 'r') as file:
            for line in file:
                for word in line.split(' '):
                    stripped_word = word.strip(chars_to_strip)
                    if self._strategy.check(stripped_word):
                        self._callback(stripped_word)


class StrategyPattern:
    """
    Runs the strategies
    """

    def run(self):
        """
        Use each of the strategies on the file
        """
        context = Context()
        filename = 'foo.txt'

        print('\nDefault:')
        context.filter(filename)

        print('\nStarts with "t":')
        context.change_strategy(StartsWithT())
        context.filter(filename)

        print('\nLonger than 5:')
        context.change_strategy(LongerThan5())
        context.filter(filename)

        print('\nPalindromes:')
        context.change_strategy(Palindrome())
        context.filter(filename)


if __name__ == '__main__':
    sp = StrategyPattern()
    sp.run()
