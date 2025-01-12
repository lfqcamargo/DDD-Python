from abc import ABC, abstractmethod


class Encrypter(ABC):

    @abstractmethod
    def encrypt(self, payload: str | None) -> str:
        pass

    def hash_comparer(self, plain: str, hash: str) -> bool:
        pass

    def hash_generator(self, plain: str) -> str:
        pass
