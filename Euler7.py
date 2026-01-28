import numpy as np
from time import perf_counter

def Erat(N):
    """
    The Sieve of Eratosthenes implemented with numpy arrays
    Returns the list of primes lower or equal than N
    """
    if N == 0 or N == 1 : return []
    elif N == 2: return [2]
    elif N == 3: return [2,3]
    else:
        N_bool = np.array([True]*(N+1))
        N_bool[0] = False
        N_bool[1] = False
        #N_bool[2] = True
        #N_bool[3] = True
        N_bool[2**2::2] = False # eiminating even numbers
        p = 3
        while p*p <= N:
            # start from p**2
            # because all the smaller composites have factors <p
            # and are already eliminated in previous steps
            N_bool[p**2::p] = False # python doesn't care if ::p goes beyond existing array
            p = p + 2 # only odd numbers can be primes larger than 3
            while not N_bool[p]:
                p = p + 2 # skip p if it has already been eliminated in previous steps
    # returns indices of nonzero elements, which in this case
    # ARE the correcponding natural numbers, which were not eliminated
    # Have to use index [0], because for technical reasons it produces a 2D array
    return list(np.nonzero(N_bool)[0]) 

def EratM(N):
    """
    The Sieve of Eratosthenes implemented with numpy arrays
    Returns the list of primes lower or equal than N
    """
    if N < 11:
        first_primes = ([],[],[2],[2,3],[2,3],[2,3,5],[2,3,5],[2,3,5,7],[2,3,5,7],[2,3,5,7],[2,3,5,7])
        return(first_primes[N]) 
    else:
        N_bool = np.array([True]*(N+1))
        N_bool[0] = False
        N_bool[1] = False
        N_bool[2**2::2] = False # eiminating even numbers
        N_bool[3**2::3] = False # eiminating multiples of 3
        p = 5
        while p*p <= N:
            # start from p**2
            # because all the smaller composites have factors <p
            # and are already eliminated in previous steps
            if N_bool[p]:
                N_bool[p**2::p] = False # python doesn't care if ::p goes beyond existing array
            if N_bool[p+2]:
                N_bool[(p+2)**2::(p+2)] = False
            p = p + 6 # we can move in steps of 6
    # returns indices of nonzero elements, which in this case
    # ARE the correcponding natural numbers, which were not eliminated
    # Have to use index [0], because for technical reasons it produces a 2D array
    return list(np.nonzero(N_bool)[0]) 

N = 2*10**8 # should NOT exceed 10**9

start1 = perf_counter()
primes1 = Erat(N)
end1 = perf_counter()

start2 = perf_counter()
primes2 = EratM(N)
end2 = perf_counter()

print(len(primes1), len(primes2), 'primes below', N)

n = 10000001
print(n, 'th prime is', primes1[n-1], primes2[n-1])

print('Erat:', end1 - start1, 'EratM:', end2 - start2,'sec')

