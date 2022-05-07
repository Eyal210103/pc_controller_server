from commands.base_command import BaseCommand
from utils.application_launcher import launch_application
import logging


class LaunchApplicationCommand(BaseCommand):
    @staticmethod
    def perform_command(args: list) -> str:
        try:
            launch_application(args[0])
        except Exception as e:
            logging.error(e)
            return f"ERROR {e}"
