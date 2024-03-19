from modules import user as u, moderator as m, gifimage as gifim
import time


def main():
    user1 = u.User(username="John", password="azerty123")
    modo1 = m.moderator.Moderator(username="Edward(moderator)", password="HelloWorld!")

    python_thread = user1.make_thread(title="What is Python?", content="Hello, I want to know what is Python?")
    python_thread.display()
    time.sleep(5)

    modo1.post(thread=python_thread, content="Not an animal for sure! It's a programming language.")
    python_thread.display()
    time.sleep(5)

    irrelevant_post = user1.post(thread=python_thread, content="Do you have air conditioning?")
    python_thread.display()
    time.sleep(5)

    response = modo1.post(thread=python_thread, content="Not relevant here.")
    python_thread.display()
    time.sleep(2)

    print("Deletion of irrelevant posts... loading...")

    time.sleep(5)
    modo1.delete(python_thread, irrelevant_post)
    modo1.delete(python_thread, response)
    python_thread.display()
    time.sleep(5)

    sorry_gif = gifim.GIFImage(name="sorry", size=3, kind="GIF")
    user1.post(thread=python_thread, content="Sorry, my bad...", file=sorry_gif)
    python_thread.display()
    time.sleep(5)

    modo1.post(thread=python_thread, content=";)")
    python_thread.display()


if __name__ == "__main__":
    main()
