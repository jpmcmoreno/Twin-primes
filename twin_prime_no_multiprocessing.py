import numpy as np
import time

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

if __name__ == '__main__':
  for i in range(0,len(m_numbers)):
    finding_twin_primes(m_numbers[i],n_numbers[i])
  t1 = time.time()
  print('Execution time', t1-t0 ,'s, using', 1 ,'Processes')