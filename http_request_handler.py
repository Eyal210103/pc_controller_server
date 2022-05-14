import json
import logging
import socketserver
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler
from typing import Tuple

from command_handler import CommandHandler
from exceptions.incompatible_command_type_error import IncompatibleCommandTypeError
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

        def do_POST(self) -> None:
            data = self.rfile.read().decode()
            try:
                json_dict = json.decoder.JSONDecoder().decode(data)
                logging.info(str(json_dict))
                result_data = self.command_handler.handle_command(json_dict['type'],
                                                                  *json_dict['args'] if 'args' in json_dict else None)
                self.create_ok(result_data)
            except IncompatibleCommandTypeError as e:
                logging.error(e)
                self.send_error(HTTPStatus.BAD_REQUEST, "Bad Command Type")
            except Exception as e:
                logging.error(e)
                self.send_response(HTTPStatus.BAD_REQUEST)
            self.end_headers()

        def do_GET(self):
            data = self.rfile.read().decode()
            try:
                json_dict = json.decoder.JSONDecoder().decode(data)
                logging.info(str(json_dict))
                result_data = self.retriever_performer.perform(json_dict['type'])
                self.create_ok(result_data)
            except IncompatibleCommandTypeError as e:
                logging.error(e)
                self.send_error(HTTPStatus.BAD_REQUEST, "Bad Retriever Type")
            except Exception as e:
                logging.error(e)
                self.send_response(HTTPStatus.BAD_REQUEST)
            self.end_headers()

    return PCControllerRequestHandler
