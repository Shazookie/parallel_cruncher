import math
import time

def isPrime(n):
    if n <= 1: 
        return False
    #for this next one, we do int to make it not a float so we can calculate time. and do plus one to fix the obo 
    for i in range (2, int(math.sqrt(n))+1): #for the range from 2 to the square root of the number we are asking about. cuts down on time for sqrt
        if n % i == 0: #if it can be divided cleanly be any of the numbers before it, it is not prime
          return False
        
    return True



# how to partition a litst
data = list(range(1, 1000000))
chunk_a = data[:25]
chunk_b = data[25:50]
chunk_c = data[50:75]
chunk_d = data[75:100]

# how to assign lists with specific instructions
# tenCount_data = [x for x in data if x % 2 == 0 and x % 5 == 0] #to make a list of all things divisable by tens

if __name__ == "__main__":
    # Your code that actually DOES things goes here

    start_time_prime = time.perf_counter() # starts timer

    prime_data = [x for x in data if isPrime(x) == True] #it it is prime then add it to the list

    end_time_prime = time.perf_counter() # ends the timer





    # Verification Output
    #print(f"Filtered: {tenCount_data}")
    #print(f"Counts: {counts}")
    #print (f"First bit: {chunk_a}")
    #print (f"last bit: {chunk_d}")
    

    #print (f"Primes: {prime_data}")
    print (f"Single thread time-elapsed: {end_time_prime - start_time_prime} (in seconds)")

