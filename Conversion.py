import numpy as np
import pandas as pd

order = input()
order1 = order.split()

m = int(order1[0])
n = int(order1[1])

list1 = input()
input_list = list1.split()

if m*n == len(input_list):
    # Write your logic here
    arr1 = np.array(input_list)
    arr2 = arr1.reshape(m,n)
    df1 = pd.DataFrame(arr2)
    print(df1)
else:
    print("Weird Order!")
