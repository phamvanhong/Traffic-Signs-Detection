import random
import shutil
import os
import cv2
from src.common.configs import *
from src.common.constans import *
import sys
# Replace the path with the path to the root directory of the project in your desktop
sys.path.append(
    r"E:\Traffic_Sign_Detection Thesis\Thesis---Traffic-Sign-Detection")


class DataCollectorAndDivider:
    def __init__(self, video_path: str, folder_frames_path: str, folder_divided_path: str) -> None:
        """
        Initialize the DataCollectorAndDivider object
        Args:
            video_path (str): The path to the video file
            folder_frames_path (str): The path to the folder to store extracted frames
            folder_divided_path (str): The path to the folder to store divided dataset
        """
        self.video_path = video_path
        self.folder_frames_path = folder_frames_path
        self.folder_divided_path = folder_divided_path

    def extract_frame(self) -> None:
        """
        Extract frames from the video and save them as images"""
        # Create the output folder if it doesn't exist
        if not os.path.exists(self.folder_frames_path):
            os.makedirs(self.folder_frames_path)

        # Open the video file
        video = cv2.VideoCapture(self.video_path)

        # Get the total number of frames in the video
        frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

        # Convert each frame to an image and save it
        for i in range(frame_count):
            ret, frame = video.read()
            if ret:
                image_path = os.path.join(
                    self.folder_frames_path, f"image_{i}.jpg")
                cv2.imwrite(image_path, frame)

    def split_dataset(self, train_ratio=0.7, test_ratio=0.15, valid_ratio=0.15):
        """
        Split a dataset into train, test, and validation sets
        Args:
            train_ratio (float): The ratio of the training set (default is 0.7)
            test_ratio (float): The ratio of the test set (default is 0.15)
            valid_ratio (float): The ratio of the validation set (default is 0.15)
        """
        # Create output folders if they don't exist
        for folder in [TRAIN, TEST, VALID]:
            os.makedirs(os.path.join(
                self.folder_divided_path, folder), exist_ok=True)

        # Get the list of image files
        image_files = [f for f in os.listdir(
            self.folder_frames_path) if f.endswith(JPG) or f.endswith(PNG)]

        # Shuffle the list of image files
        random.shuffle(image_files)

        # Calculate the number of images for each split
        num_images = len(image_files)
        num_train = int(train_ratio * num_images)
        num_test = int(test_ratio * num_images)
        num_valid = num_images - num_train - num_test

        # Split the image files into train, test, and validation sets
        train_images = image_files[:num_train]
        test_images = image_files[num_train:num_train + num_test]
        valid_images = image_files[num_train + num_test:]

        # Copy images to their respective folders
        for img_file in train_images:
            shutil.copy(os.path.join(self.folder_frames_path, img_file),
                        os.path.join(self.folder_divided_path, TRAIN, img_file))
        for img_file in test_images:
            shutil.copy(os.path.join(self.folder_frames_path, img_file),
                        os.path.join(self.folder_divided_path, TEST, img_file))
        for img_file in valid_images:
            shutil.copy(os.path.join(self.folder_frames_path, img_file),
                        os.path.join(self.folder_divided_path, VALID, img_file))
