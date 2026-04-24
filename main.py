import math

def isPrime(n):
    if n <= 1: 
        return False
    for i in range (2, n): #for the range from 2 to the number we are asking about
        if n % i == 0: #if it can be divided cleanly be any of the numbers before it, it is not prime
          return False
        
    return True



# Task 1: List Partitioning
data = list(range(1, 101))
chunk_a = data[:25]
chunk_b = data[25:50]
chunk_c = data[50:75]
chunk_d = data[75:100]

# Task 2: List Comprehension
tenCount_data = [x for x in data if x % 2 == 0 and x % 5 == 0]
prime_data = [x for x in data if isPrime(x) == True] #it it is prime then add it to the list

# Task 3: Dictionary Counts
entry_log = ['start', 'process', 'process', 'error', 'process', 'stop']
counts = {}
for entry in entry_log:
    counts[entry] = counts.get(entry, 0) + 1




# Verification Output
#print(f"Filtered: {tenCount_data}")
#print(f"Counts: {counts}")
#print (f"First bit: {chunk_a}")
#print (f"last bit: {chunk_d}")
print (f"Primes: {prime_data}")