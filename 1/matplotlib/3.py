# -*- coding:UTF-8 -*-
"""
作者:吕瑞承
日期:2021年04月01日16时
"""

from matplotlib import pyplot as plt
from matplotlib import rc

rc("font", family='MicroSoft YaHei', weight='bold', size=12)

x = range(11, 31)
y = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
z = [1, 2, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]

plt.figure(figsize=(20, 10), dpi=80)

plt.plot(x, y, label="自己", color='r')
plt.plot(x, z, label="其他", color='b')

_xtick_labers = ["{}岁".format(i) for i in x]
plt.xticks(x, _xtick_labers)
plt.yticks(range(0, 7))

plt.grid(alpha=0.3)

# 添加图例
plt.legend(loc=0)

plt.savefig("./t3.png")

plt.show()
