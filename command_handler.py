from commands.shell_command import ShellCommand
from commands.put_file_command import PutFileCommand
from exceptions.incompatible_command_type_error import IncompatibleCommandTypeError
from consts import *


class CommandHandler:
    TYPE_TO_CLASS = {
        SHELL_COMMAND_TYPE: ShellCommand,
        PUT_FILE_COMMAND_TYPE: PutFileCommand
    }

    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def handle_command(command_type: str, command: str, args=None) -> str:
        if args is None:
            args = []
        if command_type in CommandHandler.TYPE_TO_CLASS:
            return CommandHandler.TYPE_TO_CLASS[command_type]().perform_command(command, args)
        raise IncompatibleCommandTypeError(command_type)
