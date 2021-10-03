"""
Module for demonstrating the state pattern
"""
import abc
import traceback as tb


class State(abc.ABC):
    """
    Abstract base class for states
    """

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

    @abc.abstractmethod
    def close(self) -> 'State':
        pass

    @abc.abstractmethod
    def combination(self) -> 'State':
        pass

    @abc.abstractmethod
    def error(self) -> 'State':
        pass

    @abc.abstractmethod
    def lock(self) -> 'State':
        pass

    @abc.abstractmethod
    def open(self) -> 'State':
        pass

    @abc.abstractmethod
    def unlock(self) -> 'State':
        pass
