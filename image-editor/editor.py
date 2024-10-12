import os
from PIL import Image, ImageFilter, ImageEnhance
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class Editor:
    def __init__(self, picture_box, file_list):
        self.image = None
        self.original = None
        self.filename = None
        self.save_folder = "edits/"
        self.working_directory = ""
        self.picture_box = picture_box
        self.file_list = file_list

    def set_working_directory(self, directory):
        self.working_directory = directory

    def load_file_list(self):
        extension = [".svg", ".jpg", ".jpeg", ".png"]
        filenames = [
            file
            for file in os.listdir(self.working_directory)
            if file.endswith(tuple(extension))
        ]
        self.file_list.clear()
        for filename in filenames:
            self.file_list.addItem(filename)

    def load_image(self, filename):
        self.filename = filename
        fullname = os.path.join(self.working_directory, self.filename)
        self.image = Image.open(fullname)
        self.original = self.image.copy()

    def save_image(self):
        path = os.path.join(self.working_directory, self.save_folder)
        if not os.path.exists(path):
            os.makedirs(path)
        fullname = os.path.join(path, self.filename)
        self.image.save(fullname)

    def show_image(self):
        image_path = os.path.join(
            self.working_directory, self.save_folder, self.filename
        )
        pixmap = QPixmap(image_path)
        w, h = self.picture_box.width(), self.picture_box.height()
        pixmap = pixmap.scaled(w, h, Qt.KeepAspectRatio)
        self.picture_box.setPixmap(pixmap)

    def apply_filter(self, filter_name):
        if filter_name == "Original":
            self.image = self.original.copy()
        else:
            filter_mapping = {
                "Gray": lambda img: img.convert("L"),
                "Saturation": lambda img: ImageEnhance.Color(img).enhance(1.2),
                "Contrast": lambda img: ImageEnhance.Contrast(img).enhance(1.2),
                "Blur": lambda img: img.filter(ImageFilter.BLUR),
                "Left": lambda img: img.transpose(Image.ROTATE_90),
                "Right": lambda img: img.transpose(Image.ROTATE_270),
                "Mirror": lambda img: img.transpose(Image.FLIP_LEFT_RIGHT),
                "Sharpness": lambda img: img.filter(ImageFilter.SHARPEN),
            }
            self.image = filter_mapping[filter_name](self.image)
        self.save_image()
        self.show_image()

    def gray(self):
        self.image = self.image.convert("L")
        self.save_image()
        self.show_image()

    def left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.save_image()
        self.show_image()

    def right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.save_image()
        self.show_image()

    def mirror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.save_image()
        self.show_image()

    def sharpen(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.save_image()
        self.show_image()

    def blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.save_image()
        self.show_image()

    def saturation(self):
        self.image = ImageEnhance.Color(self.image).enhance(1.2)
        self.save_image()
        self.show_image()

    def contrast(self):
        self.image = ImageEnhance.Contrast(self.image).enhance(1.2)
        self.save_image()
        self.show_image()
