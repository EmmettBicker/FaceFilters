import time 
__start_time = time.time()
global __held_time
__held_time = time.time()
def update_held_time():
    global __held_time
    __held_time = time.time()

def get_held_time():
    global __held_time
    return __held_time