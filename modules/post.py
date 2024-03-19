class Post:
    def __init__(self, user, time_posted, content):
        self.user = user
        self.time_posted = time_posted
        self.content = content

    def display(self):
        print(f"--Message sent {self.time_posted} by {self.user} --")
        print(self.content)
