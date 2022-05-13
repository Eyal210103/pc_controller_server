import socketserver
import json
import logging
from http.server import BaseHTTPRequestHandler
from http import HTTPStatus
from typing import Type, Tuple
from command_handler import CommandHandler
from retrievers_performers import RetrieversPerformer
from exceptions.incompatible_command_type_error import IncompatibleCommandTypeError


def get_request_handler(command_handler: CommandHandler, retriever_performer: RetrieversPerformer):
    class PCControllerRequestHandler(BaseHTTPRequestHandler):

        def __init__(self, request: bytes, client_address: Tuple[str, int], server: socketserver.BaseServer) -> None:
            self.command_handler: CommandHandler = command_handler
            self.retriever_performer = retriever_performer
            super().__init__(request, client_address, server)

        def create_ok(self, data_to_send):
            self.send_response(HTTPStatus.OK)
            self.wfile.write(data_to_send.encode())  # change to json object
            self.send_header("Content-Length", str(len(data_to_send.encode())))

        def do_POST(self) -> None:
            data = self.rfile.read().decode()
            try:
                json_dict = json.decoder.JSONDecoder().decode(data)
                logging.info(str(json_dict))
                result = self.command_handler.handle_command(json_dict['type'], json_dict['args'])
                self.create_ok(result)
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
                result = self.retriever_performer.perform(json_dict['type'], json_dict['args'])
                self.create_ok(result)
            except IncompatibleCommandTypeError as e:
                logging.error(e)
                self.send_error(HTTPStatus.BAD_REQUEST, "Bad Retriever Type")
            except Exception as e:
                logging.error(e)
                self.send_response(HTTPStatus.BAD_REQUEST)
            self.end_headers()

    return PCControllerRequestHandler
