from src.model.data_augment import DataAugment
from src.common.configs import *
from src.common.constans import *
import sys
sys.path.append(
    r'E:\Traffic_Sign_Detection Thesis\Thesis---Traffic-Sign-Detection')


def main():
    train_data_folder = r"cropped_images"
    test_data_folder = r"data\VN_Traffic_Sign_Robo\test\images"
    valid_data_folder = r"data\VN_Traffic_Sign_Robo\valid\images"

    resize = r"augment_image\resize"
    blur = r"augment_image\blur"
    noise = r"augment_image\noise"
    high_contrast = r"augment_image\high_contrast"
    low_contrast = r"augment_image\low_contrast"
    darkness = r"augment_image\darkness"
    brightness = r"augment_image\brightness"

    # Generate data
    resize_aug = DataAugment(train_data_folder, resize)
    resize_aug.process_images(resize_aug.resize)

    blur_aug = DataAugment(resize, blur)
    blur_aug.process_images(blur_aug.add_blur)

    noise_aug = DataAugment(resize, noise)
    noise_aug.process_images(noise_aug.add_noise)

    high_contrast_aug = DataAugment(resize, high_contrast)
    high_contrast_aug.process_images(high_contrast_aug.change_contrast, 2.0)

    low_contrast_aug = DataAugment(resize, low_contrast)
    low_contrast_aug.process_images(low_contrast_aug.change_contrast, 0.5)

    darkness_aug = DataAugment(resize, darkness)
    darkness_aug.process_images(darkness_aug.modified_color, 0.5)

    brightness_aug = DataAugment(resize, brightness)
    brightness_aug.process_images(brightness_aug.modified_color, 2.0)


if __name__ == "__main__":
    main()
