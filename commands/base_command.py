from abc import abstractmethod


class BaseCommand:
    @staticmethod
    @abstractmethod
    def perform_command(command: str, args: list):
        raise NotImplementedError
