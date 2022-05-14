from retrievers.base_retriever import BaseRetriever
from retrievers.dispatchers.software_list_dispatcher import SoftwareListDispatcher


class SoftwareListRetriever(BaseRetriever):
    @staticmethod
    def get():
        return SoftwareListDispatcher.dispatch()


if __name__ == '__main__':
    print(SoftwareListRetriever.get())
