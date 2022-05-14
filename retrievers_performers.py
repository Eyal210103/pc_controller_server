from consts import *
from retrievers.software_list_retriever import SoftwareListRetriever
from exceptions.incompatible_retriever_type_error import IncompatibleRetrieverTypeError


class RetrieversPerformer:
    TYPE_TO_CLASS = {
        GET_SOFTWARE_LIST_RETRIEVERS_TYPE: SoftwareListRetriever
    }

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def perform(retriever_type):
        if retriever_type in RetrieversPerformer.TYPE_TO_CLASS:
            return RetrieversPerformer.TYPE_TO_CLASS[retriever_type]()
        raise IncompatibleRetrieverTypeError
