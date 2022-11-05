import pandas as pd
import matplotlib.pyplot as plt


def read_data(ind_up_to, col_var, col_perf):
    data = []
    for i in range(ind_up_to + 1):
        data.append(pd.read_csv(f'data/{i}.csv'))
    data = pd.concat(data)
    data_var = data[col_var]
    data_perf = data[col_perf]
    return data_var, data_perf


def scatter(x, y):
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y)
    plt.show()

