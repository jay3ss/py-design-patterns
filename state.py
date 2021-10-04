"""
Module for demonstrating the state pattern
"""
import abc
import traceback as tb


class State(abc.ABC):
    """
    Abstract base class for states
    """

    _instance = None

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
    def close() -> 'State':
        pass

    @abc.abstractstaticmethod
    def combination() -> 'State':
        pass

    @abc.abstractstaticmethod
    def error() -> 'State':
        pass

    @abc.abstractstaticmethod
    def lock() -> 'State':
        pass

    @abc.abstractstaticmethod
    def open() -> 'State':
        pass

    @abc.abstractstaticmethod
    def unlock() -> 'State':
        pass


class AwaitingCombination(State):

    def enter() -> 'State':
        if AwaitingCombination._instance is None:
            AwaitingCombination._instance = AwaitingCombination()

        return AwaitingCombination._instance

    def combination() -> 'State':
        return Closed.enter()

    def error() -> 'State':
        return Locked.enter()

    def close() -> 'State':
        pass

    def lock() -> 'State':
        pass

    def open() -> 'State':
        pass

    def unlock() -> 'State':
        pass


class Closed(State):

    def enter() -> 'State':
        if Closed._instance is None:
            Closed._instance = Closed()

        return Closed._instance

    def combination() -> 'State':
        pass

    def error() -> 'State':
        pass

    def close() -> 'State':
        pass

    def lock() -> 'State':
        return Locked.enter()

    def open() -> 'State':
        return Opened.enter()

    def unlock() -> 'State':
        pass


class Locked(State):

    def enter() -> 'State':
        if Locked._instance is None:
            Locked._instance = Locked()

        return Locked._instance

    def combination() -> 'State':
        pass

    def error() -> 'State':
        pass

    def close() -> 'State':
        pass

    def lock() -> 'State':
        pass

    def open() -> 'State':
        pass

    def unlock() -> 'State':
        return AwaitingCombination.enter()


class Opened(State):

    def enter() -> 'State':
        if Opened._instance is None:
            Opened._instance = Opened()

        return Opened._instance

    def combination() -> 'State':
        return Closed.enter()

    def error() -> 'State':
        pass

    def close() -> 'State':
        return Closed.enter()

    def lock() -> 'State':
        pass

    def open() -> 'State':
        pass

    def unlock() -> 'State':
        pass


class Context:
    def __init__(self) -> None:
        self._state = Closed.enter()

    def handle_event(self, command):
        old_state = self._state
        self._state = self._state.handle_event(command)

        if not old_state == self._state:
            state_name = type(self._state).__name__
            print(f'\tChanged state to: {state_name}')
