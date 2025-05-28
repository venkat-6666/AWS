# main.py
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

if __name__ == "__main__":
    user_name = "Developer"
    print(greet(user_name))
    
    result = add(5, 3)
    print(f"The result of 5 + 3 is: {result}")
