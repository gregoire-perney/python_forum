from ocr_python_POO.ex2_forum.modules import post as p


class FilePost(p.Post):
    def __init__(self, file, user, time_posted, content):
        super().__init__(user, time_posted, content)
        self.file = file

    def display(self):
        super().display()
        print("Attached file:")
        self.file.display()
