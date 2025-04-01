""" Works out the Lowest Common Multiple of a sequence of integers """

import time

def get_max_from_user():
    """ Asks the user for the max number in the sequence

    And does some error checking"""
    n_max_str = input("Enter the max number of the sequence: ")
    try:
        n_max = int(n_max_str)
    except:
        print("You'll need to enter an integer")
    else:
        return n_max

def generate_sequence(n_max):
    """ Generates the sequence we will be working with """
    return list(range(1, n_max + 1))

def display_time_taken(t_start, t_end):
    """ Displays time taken in nice units """
    billion = 1000000000
    million = 1000000
    thousand = 1000
    t = t_end - t_start
    if t > billion:
        print(round(t / billion, 2), "s")
    elif t > million:
        print(round(t / million, 2), "ms")
    elif t > thousand:
        print(round(t / thousand, 2), "us")
    else:
        print(t, "ns")

def simple_function(ns):    
    """ This is the simple but slow method """
    t_start = time.monotonic_ns()
    
    n_max = max(ns)
    candidate = n_max
    found = False
    
    while not found:
        found = True
        for n in ns:
            if candidate % n != 0:
                found = False
                candidate += n_max
                break
            
    t_end = time.monotonic_ns()
    
    display_time_taken(t_start, t_end)    
    return candidate

def optimal_function(ns):
    """ This is an attempt at a more optimal function """
    t_start = time.monotonic_ns()
    
    n_max = max(ns)
    candidate = n_max
    found = False

    # Complicated Code Goes Here
    
    t_end = time.monotonic_ns()
    
    display_time_taken(t_start, t_end)
    return candidate

if __name__ == "__main__":
    n_max = get_max_from_user()
    if n_max:
        ns = generate_sequence(n_max)
        if n_max <= 20:
            print("Using Simple Function")
            lcm = simple_function(ns)
            print("Found LCM:", lcm)
        else:
            print("Should not use simple function for numbers greater than 20")
    else:
        print("Nothing to do")
    

