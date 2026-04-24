import math
import time
from multiprocessing import Pool, cpu_count #will use the max about of cores available


def isPrime(n):
    if n <= 1: 
        return False
    #for this next one, we do int to make it not a float so we can calculate time. and do plus one to fix the obo 
    for i in range (2, int(math.sqrt(n))+1): #for the range from 2 to the square root of the number we are asking about. cuts down on time for sqrt
        if n % i == 0: #if it can be divided cleanly be any of the numbers before it, it is not prime
          return False
        
    return True

def PrimeList(n): ##helps us get our actual list of all primes, not just a list of boolean values
    if isPrime(n) == True:
        return n
    else:
        return None



data = list(range(1, 1000000)) #this is global


# how to assign lists with specific instructions
# tenCount_data = [x for x in data if x % 2 == 0 and x % 5 == 0] #to make a list of all things divisable by tens

if __name__ == "__main__":
    #  code that actually DOES things goes here

#############// SINGLE THREADED //############
    start_time_prime = time.perf_counter() # starts timer

    prime_data = [x for x in data if isPrime(x) == True] #it it is prime then add it to the list

    end_time_prime = time.perf_counter() # ends the timer


#############// MULTI THREADED //############


    start_time_prime_threaded = time.perf_counter()

    with Pool(cpu_count()) as Workers: #auto divides the work into equal parts for all available cores

        threaded_prime = Workers.map(PrimeList, data) #auto does the logic, checks is prime for each member of data

        CleanPrimeList = [p for p in threaded_prime if p is not None] #cleans away the 'none' variables

    end_time_prime_threaded = time.perf_counter()





    # Verification Output
    #print(f"Filtered: {tenCount_data}")
    #print(f"Counts: {counts}")
    #print (f"First bit: {chunk_a}")
    #print (f"last bit: {chunk_d}")
    

    #print (f"Primes: {prime_data}")
    print (f"Num of Primes for Single: {len(prime_data)}")
    print (f"Single thread time-elapsed: {end_time_prime - start_time_prime} (in seconds)")
    print (f"Num of Primes for Multi: {len(CleanPrimeList)}")
    print (f"Multi thread time-elapsed: {end_time_prime_threaded - start_time_prime_threaded} (in seconds)")

