import os

def rename_files_in_folder(folder_path: str, file_name: str, new_character: str) -> None:
    """
    Rename files in a folder by adding a new character to the file name
    Args:
        folder_path (str): The path to the folder to rename files
        file_name (str): The name of the file to rename
        new_character (str): The new character to add to the file name"""
    for filename in os.listdir(folder_path):
        if filename.endswith(file_name):
            # Add a '.' before the file extension
            new_filename = filename.rsplit('.', 1)[0] + new_character + '.' + filename.rsplit('.', 1)[1]
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

def main():
    resize = r"augment_image\resize"
    blur = r"augment_image\blur"
    noise = r"augment_image\noise"
    high_contrast = r"augment_image\high_contrast"
    low_contrast = r"augment_image\low_contrast"
    darkness = r"augment_image\darkness"
    brightness = r"augment_image\brightness"

    file_name = '.jpg'
    rename_files_in_folder(resize, file_name, "resize")
    rename_files_in_folder(blur, file_name, "blur")
    rename_files_in_folder(noise, file_name, "noise")
    rename_files_in_folder(high_contrast, file_name, "high_con")
    rename_files_in_folder(low_contrast, file_name, "low_con")
    rename_files_in_folder(darkness, file_name, "darkness")
    rename_files_in_folder(brightness, file_name, "brightness")

    resize = r"adjust_annotation\resize"
    blur = r"adjust_annotation\blur"
    noise = r"adjust_annotation\noise"
    high_contrast = r"adjust_annotation\high_contrast"
    low_contrast = r"adjust_annotation\low_contrast"
    darkness = r"adjust_annotation\darkness"
    brightness = r"adjust_annotation\brightness"

    file_name = '.txt'
    rename_files_in_folder(resize, file_name, "resize")
    rename_files_in_folder(blur, file_name, "blur")
    rename_files_in_folder(noise, file_name, "noise")
    rename_files_in_folder(high_contrast, file_name, "high_con")
    rename_files_in_folder(low_contrast, file_name, "low_con")
    rename_files_in_folder(darkness, file_name, "darkness")
    rename_files_in_folder(brightness, file_name, "brightness")

if __name__ == "__main__":
    main()