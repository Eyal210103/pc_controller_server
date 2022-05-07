from commands.base_command import BaseCommand
import subprocess
import logging


class ShellCommand(BaseCommand):
    @staticmethod
    def perform_command(command: str, args: list) -> str:
        try:
            result = subprocess.check_output(command, shell=True).decode()
            logging.info(result)
            return result
        except Exception as e:
            logging.error(e)
            return f"ERROR {e}"
