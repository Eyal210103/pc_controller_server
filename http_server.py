import logging
from http_request_handler import get_request_handler
from typing import Tuple
from http.server import HTTPServer
from command_handler import CommandHandler

logging.basicConfig(level=logging.DEBUG)

BINDING_ADDRESS = ('127.0.0.1', 8080)


class PCControllerHTTPServer:

    def __init__(self, binding_address: Tuple[str, int], command_handler=CommandHandler()) -> None:
        self.server = HTTPServer(binding_address, get_request_handler(command_handler))

    def serve(self) -> None:
        self.server.serve_forever()

    def shutdown(self) -> None:
        self.server.shutdown()


def main():
    server = PCControllerHTTPServer(BINDING_ADDRESS)
    server.serve()


if __name__ == '__main__':
    main()
