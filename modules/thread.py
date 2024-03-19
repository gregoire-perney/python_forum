class Thread:
    def __init__(self, title, time_posted, post):
        self.title = title
        self.time_posted = time_posted
        self.posts = [post]

    def display(self):
        print("----- THREAD -----")
        print(f"Title: {self.title}, Date: {self.time_posted}")
        print()
        for post in self.posts:
            post.display()
            print()
        print("------------------")

    def add_post(self, post):
        self.posts.append(post)
