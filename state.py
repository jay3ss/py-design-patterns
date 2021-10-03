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


class AwaitingCombination(State):

    def enter(self) -> 'State':
        if self._instance is None:
            self._instance = AwaitingCombination()

        return self._instance

    def combination(self) -> 'State':
        return Closed.enter()

    def error(self) -> 'State':
        return Locked.enter()

    def close(self) -> 'State':
        pass

    def lock(self) -> 'State':
        pass

    def open(self) -> 'State':
        pass

    def unlock(self) -> 'State':
        pass


class Closed(State):

    def enter(self) -> 'State':
        if self._instance is None:
            self._instance = Closed()

        return self._instance

    def combination(self) -> 'State':
        return Closed.enter()

    def error(self) -> 'State':
        return Locked.enter()

    def close(self) -> 'State':
        pass

    def lock(self) -> 'State':
        return Locked.enter()

    def open(self) -> 'State':
        return Opened.enter()

    def unlock(self) -> 'State':
        pass


class Locked(State):

    def enter(self) -> 'State':
        if self._instance is None:
            self._instance = Locked()

        return self._instance

    def combination(self) -> 'State':
        return Closed.enter()

    def error(self) -> 'State':
        return Locked.enter()

    def close(self) -> 'State':
        pass

    def lock(self) -> 'State':
        return Locked.enter()

    def open(self) -> 'State':
        return Opened.enter()

    def unlock(self) -> 'State':
        return AwaitingCombination.enter()


class Opened(State):
    pass
