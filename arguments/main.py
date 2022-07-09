# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
def greet(name, greeting_template = "Hello, <name>!"):
    x = greeting_template.replace("<name>", name)
    return(x)

def force(mass, body = "earth"):
    gravity = {
        'sun'       : 274,
        'jupiter'   : 24.9,
        'neptune'   : 11.1,
        'saturn'    : 10.4,
        'earth'     : 9.8,
        'uranus'    : 8.9,
        'venus'     : 8.9,
        'mars'      : 3.7,
        'mercury'   : 3.7,
        'moon'      : 1.6,
        'pluto'     : 0.6
    }
    #x = mass * gravity[body]
    #print(f"massa = {mass}, gravity = {gravity[body]} force = {x}")
    return(mass * gravity[body])

def pull(m1, m2, d):
    gravity = 6.674 * 10 **-11
    x = gravity * ((m1 * m2)/d ** 2)
    #print(f"gravity = {gravity} en x = {x}")
    return(x)

print(greet("Remko", "Hoi, <name>!"))
force(100, "pluto")
#pull(800, 1500, 3)
pull(0.1, 5.972 * 10 ** 24, 6.371 * 10 ** 6)