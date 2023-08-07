import abc
import csv
from typing import IO, Any, Generator, Iterable


def _file_decode(file: IO[bytes]) -> Generator[str, None, None]:
    for byt in file.readlines():
        yield byt.decode()


class Parser(abc.ABC):
    @abc.abstractmethod
    def _get_data(self, file: IO[Any]) -> Iterable[list[str]]:
        ...

    def get_deals_data(self, file: IO[Any]) -> Generator[dict[str, str], None, None]:
        for row in self._get_data(file):
            if row == ["customer", "item", "total", "quantity", "date"]:
                continue
            yield {"customer": row[0], "item": row[1], "total": row[2], "quantity": row[3], "date": row[4]}


class ParserCSVBytes(Parser):
    """Parser bytes files."""

    def _get_data(self, file: IO[bytes]) -> Iterable[list[str]]:
        return csv.reader(_file_decode(file))

    def get_deals_data(self, file: IO[bytes]) -> Generator[dict[str, str], None, None]:
        return super().get_deals_data(file)


class ParserCSVText(Parser):
    """Parser bytes files."""

    def _get_data(self, file: IO[str]) -> Iterable[list[str]]:
        return csv.reader(file)

    def get_deals_data(self, file: IO[str]) -> Generator[dict[str, str], None, None]:
        return super().get_deals_data(file)
