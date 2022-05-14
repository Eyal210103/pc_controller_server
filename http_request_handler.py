import json
import logging
import socketserver
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler
from typing import Tuple, Callable

from command_handler import CommandHandler
from exceptions.incompatible_command_type_error import IncompatibleCommandTypeError
from exceptions.incompatible_retriever_type_error import IncompatibleRetrieverTypeError
from result import Result
from retrievers_performers import RetrieversPerformer


def get_request_handler(command_handler: CommandHandler, retriever_performer: RetrieversPerformer):
    class PCControllerRequestHandler(BaseHTTPRequestHandler):

        def __init__(self, request: bytes, client_address: Tuple[str, int], server: socketserver.BaseServer) -> None:
            self.command_handler: CommandHandler = command_handler
            self.retriever_performer = retriever_performer
            super().__init__(request, client_address, server)

        def create_ok(self, data_to_send):
            result_json: str = Result(data_to_send).to_json()
            self.send_response(HTTPStatus.OK)
            self.wfile.write(result_json.encode(encoding='UTF-16'))  # change to json object
            self.send_header("Content-Length", str(len(result_json)))

        def handle_single_request(self, action: Callable):
            data = self.rfile.read().decode()
            try:
                json_dict = json.decoder.JSONDecoder().decode(data)
                logging.info(str(json_dict))
                result_data = action(json_dict['type'] * json_dict['args'] if 'args' in json_dict else None)
                self.create_ok(result_data)
            except IncompatibleCommandTypeError or IncompatibleRetrieverTypeError as e:
                logging.error(e)
                self.send_error(HTTPStatus.BAD_REQUEST, "Bad Type")
            except Exception as e:
                logging.error(e)
                self.send_response(HTTPStatus.BAD_REQUEST)
            self.end_headers()

        def do_POST(self) -> None:
            self.handle_single_request(self.command_handler.handle_command)

        def do_GET(self):
            self.handle_single_request(self.retriever_performer.perform)

    return PCControllerRequestHandler
