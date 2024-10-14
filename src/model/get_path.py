import os
import re


class FilePathCollector:
    def __init__(self, img_folder: str, annotation_folder: str) -> None:
        """
        Initialize the FilePathCollector class with the image and annotation folders"""
        self.img_folder = img_folder
        self.annotation_folder = annotation_folder
        self.img_paths = []
        self.annotation_paths = []

    def numerical_sort(self, value) -> list:
        """
        Extract numbers from the file name and convert to integer
        Args:
            value (str): The file name
        Returns:
            list: List of numbers from the file name
        """
        numbers = re.compile(r'(\d+)')
        parts = numbers.split(value)
        parts[1::2] = map(int, parts[1::2])
        return parts

    def get_img_path(self) -> list:
        """
        Get the path to the image files
        Returns:
            list: List of paths to the image files
        """
        for filename in sorted(os.listdir(self.img_folder), key=self.numerical_sort):
            file_path = os.path.join(self.img_folder, filename)
            self.img_paths.append(file_path)
        return self.img_paths

    def get_annotation_path(self) -> list:
        """
        Get the path to the annotation files
        Returns:
            list: List of paths to the annotation files
        """
        for filename in sorted(os.listdir(self.annotation_folder), key=self.numerical_sort):
            file_path = os.path.join(self.annotation_folder, filename)
            self.annotation_paths.append(file_path)
        return self.annotation_paths
