from typing import Generic, TypeVar, Union

L = TypeVar("L")
R = TypeVar("R")

class Left(Generic[L, R]):
    def __init__(self, value: L) -> None:
        self.value = value

    def is_left(self) -> bool:
        return True

    def is_right(self) -> bool:
        return False


class Right(Generic[L, R]):
    def __init__(self, value: R) -> None:
        self.value = value

    def is_left(self) -> bool:
        return False

    def is_right(self) -> bool:
        return True


Either = Union[Left[L, R], Right[L, R]]

def left(value: L) -> Either[L, R]:
    return Left(value)


def right(value: R) -> Either[L, R]:
    return Right(value)
