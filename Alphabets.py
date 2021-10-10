import pandas as pd

# Convert 'inp' into a list
inp = 'abcedfghijklmnopqrstuvwxyz'
l= list(inp)

# Write your logic to take input from STDIN
a = input()
S1 = pd.Series(data=l,name=a)

# Write your logic to print output to STDOUT
print(S1)
