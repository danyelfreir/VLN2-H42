class HelloWorld:
    @classmethod
    def hello_word(cls, username):
        print(f"Hello {username}!")

if __name__ == '__main__':
    username = input("Enter your username: ")
    HelloWorld.hello_word(username)
