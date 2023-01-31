from datetime import datetime


class Log:
    def __init__(self):
        self._filename = f"logs/{datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}"

    def get_filename(self):
        return self._filename

    def add(self, message: str):
        """Add a message in the log file"""
        with open(f"{self._filename}.txt", 'a') as log_file:
            log_file.write('\n')
            log_file.write(message)
