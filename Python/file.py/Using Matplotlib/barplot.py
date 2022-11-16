import numpy as np
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,]

x_indexes = np.arange(len(ages_x))
wdth = 0.25

py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
plt.bar(x_indexes - wdth, py_dev_y, width = wdth, label='Python')

js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
plt.bar(x_indexes, js_dev_y, width = wdth, label='JavaScript')

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
plt.bar(x_indexes + wdth, dev_y, width = wdth, color='#444444', linestyle='--', label='All Devs')

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')

plt.xticks(ticks = x_indexes, labels = ages_x)

plt.legend()

plt.tight_layout()

# plt.savefig('C:\Data Analytics Professional\Week 9/Median Salary (USD) by Age Bar Graph.png')

plt.show()