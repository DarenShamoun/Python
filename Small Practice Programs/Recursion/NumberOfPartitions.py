def NumberOfPartitions(n):
    # create an empty matrix
    partitions = [[0 for i in range(n + 1)] for j in range(n + 1)]
    # set the first entry in the matrix to 1 as we always start from 1
    partitions[0][0] = 1

    # Constructs a Bell Triangle to find the number of partitions possible
    for i in range(1, n + 1):

        # Explicitly fill for j = 0
        partitions[i][0] = partitions[i - 1][i - 1]

        # the second loop finds the remaining values of j
        for j in range(1, i + 1):
            partitions[i][j] = partitions[i - 1][j - 1] + partitions[i][j - 1]

    # returns the first value in the BellTriangle which is the bell number of the previous row
    return partitions[n][0]

# the range can be changed by editing the below value and adding 1 to the value you need
for n in range(51):
    print('The number of partitions in n=', n, 'is', NumberOfPartitions(n))
