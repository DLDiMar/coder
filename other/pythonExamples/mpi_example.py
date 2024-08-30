from mpi4py import MPI
import numpy as np

# Initialize the MPI communicator
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Size of the array
n = 100

# Initialize the array on the root process (rank 0)
if rank == 0:
    data = np.arange(n, dtype='int')
else:
    data = None

# Determine the number of elements per process
elements_per_process = n // size

# Create a buffer to hold the subset of data on each process
sub_array = np.zeros(elements_per_process, dtype='int')

# Scatter the data across processes
comm.Scatter(data, sub_array, root=0)

# Each process computes the sum of its sub-array
local_sum = np.sum(sub_array)

# Gather all the local sums to the root process
total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

# The root process prints the total sum
if rank == 0:
    print(f"The total sum is: {total_sum}")
