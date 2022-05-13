from abc import abstractmethod


class BaseRetriever:
    @staticmethod
    @abstractmethod
    def get():
        raise NotImplementedError
