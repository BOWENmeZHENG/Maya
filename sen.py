import utils

col_var = ['WIDTH_mem', 'THICKNESS_mem', 'WIDTH_device', 'HEIGHT_chamber', 'HEIGHT_device', 'InnerRing', 'OuterRing']
col_perf = ['Negative Pressure Adh Force', 'Pos Pressure Adh Force']

data_var, data_perf = utils.read_data(6, col_var, col_perf)

def func(x, a, b, c):
    return a * x ** 2 + b * x + c


x_fit, yfit = utils.fitting(func, data_var['OuterRing'], data_perf['Negative Pressure Adh Force'])


utils.scatter(data_var['OuterRing'], data_perf['Negative Pressure Adh Force'], x_fit, yfit)