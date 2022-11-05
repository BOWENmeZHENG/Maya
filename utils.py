import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def read_data(ind_up_to, col_var, col_perf):
    data = []
    for i in range(ind_up_to + 1):
        data.append(pd.read_csv(f'data/{i}.csv'))
    data = pd.concat(data)
    data_var = data[col_var]
    data_perf = data[col_perf]
    return data_var, data_perf


def scatter(x, y, x_fit, yfit):
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, c='blue', s=10)
    plt.plot(x_fit, yfit, c='red', linewidth=3)
    plt.show()


def fitting(func, xdata, ydata):
    popt, *_ = curve_fit(func, xdata, ydata)
    x_fit = np.linspace(min(xdata), max(xdata), 50)
    return x_fit, func(x_fit, *popt)
