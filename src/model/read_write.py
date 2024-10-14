from src.common.constans import READ, WRITE
import os


class ReadWriteFile:
    def __init__(self, file_path: str, folder_path: str) -> None:
        """
        Initialize the ReadWriteFile class with the file path and folder path
        Args:
            file_path (str): The path to the file want to read or write
            folder_path (str): The path to the folder want to create a new file
        """
        self.file_path = file_path
        self.folder_path = folder_path

    def read_lines_in_file(self) -> list:
        """
        Read all lines in the file
        """
        with open(self.file_path, READ) as file:
            lines = file.readlines()
        return lines

    def write_to_file(self, data) -> None:
        """
        Write data to the file
        """
        with open(self.file_path, WRITE) as file:
            file.write(data)

    def create_new_file_path(self):
        """
        Create a new file path in the folder path
        """
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

        base_name = os.path.basename(self.file_path)
        new_file_path = os.path.join(self.folder_path, base_name)
        return new_file_path
