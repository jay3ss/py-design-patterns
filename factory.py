"""
An example of the factory pattern.
"""
from datetime import datetime
import pathlib
from typing import List


class DirectoryListing:
    """
    """
    _pool = dict()

    def __init__(self, path: str=None) -> None:
        self._dir = pathlib.Path(path)
        self._files = []
        self._last_time_checked = datetime.now()

    @property
    def contents(self) -> List[pathlib.Path]:
        self.update()
        return self._files

    def update(self):
        # get the last time the file was modified
        last_modified = datetime.fromtimestamp(self._dir.stat().st_mtime)

        if not last_modified == self._last_time_checked:
            self._last_time_checked = last_modified
            self._files = sorted([file for file in self._dir.iterdir()])


    @classmethod
    def create_directory_listing(cls, path: str) -> 'DirectoryListing':
        dl = cls._pool.get(path)

        if dl is None:
            dl = DirectoryListing(path)
            cls._pool[path] = dl

        return dl
