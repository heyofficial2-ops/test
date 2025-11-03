# Simple name responder

def respond_to_name(name):
    name = name.strip()
    if not name:
        return "Please enter a name."
    if name.lower() == name.lower()[::-1]:
        return f"Hi {name}! Your name is a palindrome!"
    if name.isupper():
        return f"Whoa {name}! No need to shout!"
    return f"Hello, {name.title()}! Nice to meet you."

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(respond_to_name(user_name))
