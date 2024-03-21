from modules import user as u


class Moderator(u.User):
    def edit(self, post, content):
        post.content = content

    def delete(self, thread, post):
        index = thread.posts.index(post)
        del thread.posts[index]
