from modules import filepost as fp, post as p, thread as th


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        print(f"User '{self.username}' is connected")

    def post(self, thread, content, file=None):
        if file:
            post = fp.FilePost(user=self, time_posted="Today", content=content, file=file)
        else:
            post = p.Post(user=self, time_posted="Today", content=content)
        thread.add_post(post)
        return post

    def make_thread(self, title, content):
        post = p.Post(self, time_posted="Today", content=content)
        return th.Thread(title=title, time_posted="Today", post=post)

    def __str__(self):
        return self.username
