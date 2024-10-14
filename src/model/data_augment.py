import os
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import cv2


class DataAugment:
    def __init__(self, input_folder: str, output_folder: str):
        """
        Initialize the DataAugment class with the input and output folders
        Args:
            input_folder (str): The input folder containing images
            output_folder (str): The output folder to save processed images
        """
        self.input_folder = input_folder
        self.output_folder = output_folder

    def process_images(self, operation, *arg) -> None:
        """
        Process the images in the input folder with the specified operation
        Args:
            operation (function): The operation to apply on each image
            *arg: Additional arguments to pass to the operation function
        """
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        for filename in os.listdir(self.input_folder):
            if filename.endswith('.jpg') or filename.endswith('.png'):
                img_path = os.path.join(self.input_folder, filename)

                # Apply the operation to the image
                processed_img = operation(img_path, *arg)

                output_img_path = os.path.join(self.output_folder, filename)
                processed_img.save(output_img_path)

    def resize(self, img_path: str) -> Image.Image:
        """
        Resize the input image to a smaller size (640x640)
        Args:
            img_path (str): The path to the input image
        Returns:
            PIL.Image.Image: The resized image
        """
        img = Image.open(img_path)
        return img.resize((640, 640))

    def add_noise(self, img_path: str) -> Image.Image:
        """
        Add noise to the input image
        Args:
            img_path (str): The path to the input image
        Returns:
            PIL.Image.Image: The image with added noise
        """
        img = Image.open(img_path)

        # Convert the image to numpy array
        img_arr = np.array(img)

        # Generate Gaussian noise
        noise = np.random.normal(0, 25, img_arr.shape).astype(np.uint8)

        # Add the noise to the image
        noisy_img_array = img_arr + noise

        # Ensure the noisy image array values are within the valid range (0-255)
        noisy_img_array = np.clip(noisy_img_array, 0, 255)

        # Convert the noisy image array back to an image
        return Image.fromarray(noisy_img_array)

    def add_blur(self, img_path: str) -> Image.Image:
        """
        Add blur to the input image
        Args:
            img_path (str): The path to the input image
        Returns:
            PIL.Image.Image: The image with added blur
        """
        img = Image.open(img_path)
        return img.filter(ImageFilter.GaussianBlur(radius=2))

    def rotate(self, img_path: str, angle: float) -> Image.Image:
        """
        Rotates an image (angle in degrees) and expands image to avoid cropping
        Args:
            img_path (str): The path to the input image
            angle (float): The angle to rotate the image
        Returns:
            PIL.Image.Image: The rotated image
        """
        image = cv2.imread(img_path)
        height, width = image.shape[:2]  # image shape has 3 dimensions
        # getRotationMatrix2D needs coordinates in reverse order (width, height) compared to shape
        image_center = (width / 2, height / 2)

        rotation_mat = cv2.getRotationMatrix2D(image_center, angle, 1.)

        # rotation calculates the cos and sin, taking absolutes of those.
        abs_cos = abs(rotation_mat[0, 0])
        abs_sin = abs(rotation_mat[0, 1])

        # find the new width and height bounds
        bound_w = int(height * abs_sin + width * abs_cos)
        bound_h = int(height * abs_cos + width * abs_sin)

        # subtract old image center (bringing image back to origin) and adding the new image center coordinates
        rotation_mat[0, 2] += bound_w / 2 - image_center[0]
        rotation_mat[1, 2] += bound_h / 2 - image_center[1]

        # rotate image with the new bounds and translated rotation matrix
        rotated_mat = cv2.warpAffine(image, rotation_mat, (bound_w, bound_h))
        return Image.fromarray(cv2.cvtColor(rotated_mat, cv2.COLOR_BGR2RGB))

    def change_contrast(self, img_path: str, factor: float) -> Image.Image:
        """
        Convert the input image to hight and low contrast
        Args:
            img_path (str): The path to the input image
            factor (float): The contrast value
        Returns:
            PIL.Image.Image: The image with high and low contrast
        """
        img = Image.open(img_path)
        return ImageEnhance.Contrast(img).enhance(factor)

    def modified_color(self, img_path: str, factor: float) -> Image.Image:
        """
        Modify the color of the input image
        Args:
            img_path (str): The path to the input image
            factor (float): The color value
        Returns:
            PIL.Image.Image: The image with modified color
        """
        img = Image.open(img_path)
        return ImageEnhance.Brightness(img).enhance(factor)
