import logging
from http_request_handler import get_request_handler
from typing import Tuple
from http.server import HTTPServer
from command_handler import CommandHandler
from retrievers_performers import RetrieversPerformer


class PCControllerHTTPServer:

    def __init__(self, binding_address: Tuple[str, int], command_handler=CommandHandler(),
                 retrievers_performer=RetrieversPerformer()) -> None:
        self.server = HTTPServer(binding_address, get_request_handler(command_handler, retrievers_performer))

    def serve(self) -> None:
        self.server.serve_forever()

    def shutdown(self) -> None:
        self.server.shutdown()
