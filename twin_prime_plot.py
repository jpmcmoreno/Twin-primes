import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

for i in range (1,1000000):
  if is_prime(i) and is_prime(i+2):
      x.append(i)
      y.append(i+2)

plt.xlabel("q")
plt.ylabel("p")
plt.plot(x,y, "ro")