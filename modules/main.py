# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line
import this

def wait(seconds: int):
    import time
    time.sleep(seconds)
    return

def my_sin(arg: float):
    import math
    return(math.sin(arg))

def iso_now():
    import datetime
    my_date = datetime.datetime.now()
    return(my_date.strftime("%Y-%m-%dT%H:%M"))

def platform():
    import sys
    #x = sys.platform
    #print(f"het platform is: {x}")
    return(sys.platform)

from greet import supergreeting

def supergreeting_wrapper(arg: str):
    return(supergreeting(arg))

def main():
    iso_now()
    platform()
    print(supergreeting_wrapper("Winc"))

if __name__ == '__main__':
    main()