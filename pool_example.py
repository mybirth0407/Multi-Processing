import multiprocessing
from multiprocessing import Pool
import os

def productor(data):
  print(os.getpid())
  return data[0] * data[1]


if __name__ == '__main__':
  n_processes = multiprocessing.cpu_count()
  print(n_processes)

  pool = Pool(processes=n_processes)
  # like thread pool
  # multiple argument 2d list
  result = pool.map(productor, [[1, 2],[3, 4],[5, 6]])
  print(result)
