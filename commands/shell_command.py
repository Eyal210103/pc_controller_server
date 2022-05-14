from commands.base_command import BaseCommand
import subprocess
import logging


class ShellCommand(BaseCommand):
    @staticmethod
    def perform_command(args: list) -> str:
        try:
            result = subprocess.check_output(args[0], shell=True).decode()
            logging.info(result)
            return result
        except IndexError as e:
            logging.error(e)
            return "Missing Arguments"
        except Exception as e:
            logging.error(e)
            return f"ERROR {e}"
