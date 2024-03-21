from modules import file as f


class ImageFile(f.File):
    def display(self):
        print(f"Image file '{self.name}'")
