from abc import ABC, abstractmethod


class Doctor(ABC):
    @abstractmethod
    def treat(self) -> None:
        pass
