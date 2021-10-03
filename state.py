"""
Module for demonstrating the state pattern
"""
import abc
import traceback as tb


class State(abc.ABC):
    """
    Abstract base class for states
    """

    def __init__(self) -> None:
        self._instance = None

    @abc.abstractmethod
    def handle_event(self, command: str) -> 'State':
        method = None
        state = self

        try:
            method = getattr(self, command)
            state = method()
        except AttributeError:
            print(tb.extract_tb())

        return state

    @abc.abstractstaticmethod
    def close(self) -> 'State':
        pass

    @abc.abstractstaticmethod
    def combination(self) -> 'State':
        pass

    @abc.abstractstaticmethod
    def error(self) -> 'State':
        pass

    @abc.abstractstaticmethod
    def lock(self) -> 'State':
        pass

    @abc.abstractstaticmethod
    def open(self) -> 'State':
        pass

    @abc.abstractstaticmethod
    def unlock(self) -> 'State':
        pass
