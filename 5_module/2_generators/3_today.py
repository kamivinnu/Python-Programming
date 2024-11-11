# list vs gene

# memory usage, time

import time

t1 = time.time()
l = (i**2 for i in range(10000))
t2 = time.time()
print(t2 - t1) # 0.0010101795196533203