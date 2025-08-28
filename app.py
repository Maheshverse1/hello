def greet(name):
    return f"Hello, {name}! Welcome to Git testing project."


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(greet(sys.argv[1]))
    else:
        user_name = input("Enter your name: ")
        print(greet(user_name))