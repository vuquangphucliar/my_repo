import pandas as pd
import matplotlib.pyplot as plt
# from tabulate import tabulate


data = pd.read_csv('database.csv')# Resd data from file
data.dropna(inplace=True)
# new_df = tabulate(data,headers='keys',tablefmt='psql')  # the way to  make it more visualize
# dataf = pd.DataFrame(data)
# print(dataf)
print(data)
# print(sys.getsizeof(data)/8)
# print(sys.getsizeof(new_df)/8)
