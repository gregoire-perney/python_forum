from ocr_python_POO.ex2_forum.modules import file as f


class ImageFile(f.File):
    def display(self):
        print(f"Image file '{self.name}'")
