from commands.base_command import BaseCommand
from utils.file_utils import create_file
import utils.base64_to_bytes as base64_to_bytes
import logging


class PutFileCommand(BaseCommand):
    @staticmethod
    def perform_command(command: str, args: list) -> str:
        """
        args[0] = file path
        args[1] = base64 file data
        """
        try:
            file_path: str = args[0]
            base64stream: str = args[1]
            file_byte_stream = base64_to_bytes.base64_to_bytes(base64stream)
            create_file(file_path, file_byte_stream)
            return "Succeed"
        except IndexError as e:
            logging.error(e)
            return "Missing Arguments"
        except Exception as e:
            logging.error(e)
            return f"ERROR {e}"
