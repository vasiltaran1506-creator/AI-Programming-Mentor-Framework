from abc import ABC, abstractmethod
from pathlib import Path
from datetime import datetime


class Logger(ABC):
    def __init__(self) -> None:
        pass

    def log_info(self, message: str):
        formatted_info = f"[{datetime.now()}] [INFO] {message}"
        self.process_log_message(formatted_info)

    def log_warning(self, message: str):
        formatted_warning = f"[{datetime.now()}] [WARN] {message}"
        self.process_log_message(formatted_warning)

    def log_error(self, message: str):
        formatted_error = f"[{datetime.now()}] [ERROR] {message}"
        self.process_log_message(formatted_error)

    @abstractmethod
    def process_log_message(self, message: str):
        pass



class FileLogger(Logger):
    def __init__(self, log_dir) -> None:
        self.log_dir = Path(log_dir)

        current_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        filename = f"{current_time} log.txt"

        self.full_path = self.log_dir / filename


    def process_log_message(self, message: str):
        with open(self.full_path, "a", encoding="utf-8") as file:
            file.write(f"{message}\n")


class ConsoleLogger(Logger):
    def __init__(self) -> None:
        pass

    def process_log_message(self, message: str):
        print(message)
        