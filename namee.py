def greet(name):
    if not name or name.strip() == "":
        return "No name provided."
    name = name.strip().title()
    return f"Hello, {name}!"
