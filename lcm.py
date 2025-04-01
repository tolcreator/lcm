""" Works out the Lowest Common Multiple of a sequence of integers

In particular, compares the computation time between a 'brute force'
method which checks every candidate until one is found, with one that
computes the answer directly: but has to work out the prime factors
and their frequency for every number in the sequence."""

import time

def get_max_from_user():
    """ Asks the user for the max number in the sequence

    And does some error checking"""
    n_max_str = input("Enter the max number of the sequence: ")
    try:
        n_max = int(n_max_str)
    except:
        print("You'll need to enter an integer.")
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

def get_prime_factors(num, primes):
    """ Given a list of primes, works out a dictionary giving the
        frequency of prime factors of a number

        This function also creates the list of primes as we go: If we
        find a number with no prime factors from the list, it gets added
        as the newest member of the list of primes.
        """

    factors = {}

    if num == 1:
        factors[1] = 1
        return factors
    
    new_prime = True
    
    for prime in primes:
        if prime <= num // 2:
            frequency = 0
            clone = num
            while not clone % prime:
                new_prime = False
                frequency += 1
                clone //= prime
            if frequency:
                factors[prime] = frequency
                
    if new_prime:
        factors[num] = 1
        primes.append(num)
        
    return factors
    

def optimal_function(ns):
    """ This is an attempt at a more optimal function """
    t_start = time.monotonic_ns()

    primes = []
    factor_list = []

    # List all the prime factors of each number
    for n in ns:
        factor_list.append(get_prime_factors(n, primes))

    # Generate a tally of the highest frequency of each prime factor
    prime_factor_max_frequency = {}
    for factors in factor_list:
        for prime, frequency in factors.items():
            if prime in prime_factor_max_frequency:
                if frequency > prime_factor_max_frequency[prime]:
                    prime_factor_max_frequency[prime] = frequency
            else:
                prime_factor_max_frequency[prime] = frequency

    # Now we have a list of prime factors and their frequency, multiply
    # them all out and give the answer!
    candidate = 1
    for prime, frequency in prime_factor_max_frequency.items():
        candidate *= prime ** frequency
    
    t_end = time.monotonic_ns()
    
    display_time_taken(t_start, t_end)
    return candidate

if __name__ == "__main__":
    print("This function finds the LCM (Lowest Common Multiple)")
    print("Of a sequence of integers from 1 to the max you enter.")
    n_max = get_max_from_user()
    if n_max:
        ns = generate_sequence(n_max)
        if n_max <= 20:
            candidate = simple_function(ns)
            print("Simple function Got:", candidate)
        else:
            print("Skipping simple function, too slow for large sequences")
        candidate = optimal_function(ns)
        if candidate > 1000000000:
            try:
                print("Optimal Function Got: {:.2E}".format(candidate))
            except:
                print("Result too large to display")
        else:
            print("Optimal Function Got:", candidate)        
    else:
        print("Nothing to do")
    

