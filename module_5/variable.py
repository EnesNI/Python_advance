def greet(name):
    message=f"Hello, {name}"
    print(message)

greet("vlera")

    # greet (message)

greeting="Hello"
name="Vlera"

def greet():
    global greeting
    greeting="Godbye"
    global name
    name="Alice"
    message=f"{greeting}, {name}"
    print(message)

greet()

print(greeting)
print(name)