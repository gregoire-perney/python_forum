from ocr_python_POO.ex2_forum.modules import imagefile as imf


class JPGImage(imf.ImageFile):
    def __init__(self, name, size, kind):
        super().__init__(name, size)
        self.kind = kind

    def display(self):
        print(f"{self.kind} image file: '{self.name}'")
