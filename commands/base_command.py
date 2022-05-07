from abc import abstractmethod


class BaseCommand:
    @staticmethod
    @abstractmethod
    def perform_command(args: list):
        raise NotImplementedError
