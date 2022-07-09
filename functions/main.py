# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line
def greet(name):
    return(f"Hello, {name}!")  
greet("Bob")

def add(num1, num2, num3):
    return(num1 + num2 + num3)
print(add(5,3,2))

def positive(number):
    return(number > 0)
print(positive(50))
print(positive(-50))
print(positive(0))

def negative(number):
    return(number < 0)
print(negative(50))
print(negative(-50))
print(negative(0))
