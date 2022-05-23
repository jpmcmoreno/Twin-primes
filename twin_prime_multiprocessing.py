import numpy as np
import time
import multiprocessing

def is_prime(num):
  if num <= 1:
    return False
  elif num == 2:
    return True
  if(num % 2 == 0):
    return False
  else:
    prime = True
    divisor = 3
    num_d = num
    upper_limit = np.sqrt(num_d + 1)

  while divisor <= upper_limit:
    if(num % divisor == 0):
      prime = False
    divisor +=2

  return prime

def finding_twin_primes(m,n):
  num1 = np.subtract(np.multiply(m,np.power(2,n)),1)
  num2 = np.add(np.multiply(m,np.power(2,n)),1)
  if is_prime(num1) and is_prime(num2):
     print("m=",m,",n=",n)
  

t0 = time.time()
n_cpu = multiprocessing.cpu_count()
#n_cpu = 2

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=n_cpu)
    pool.starmap(finding_twin_primes, [(m_numbers[i],n_numbers[i]) for i in range(0,len(m_numbers))])
    t1 = time.time()
    print(f'Execution time {t1 - t0} s, using {n_cpu} Processes')
    