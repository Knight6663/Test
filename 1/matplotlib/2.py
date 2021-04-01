# -*- coding:UTF-8 -*-
"""
作者:吕瑞承
日期:2021年04月01日15时
"""

# 表示10点到12点的每一分钟的气温，绘制折线图观察每一分钟的气温变化

from matplotlib import pyplot as plt
from random import *
from matplotlib import rc


# 字体设置方式
font = {'family': 'MicroSoft YaHei',
        'weight': 'bold',
        'size': 'larger'}
rc("font", family='MicroSoft YaHei', weight='bold', size=12)

x = range(0, 120)
y = [randint(20, 35) for i in range(120)]

plt.figure(figsize=(20, 10), dpi=80)

plt.plot(x, y)

# 调整x轴的刻度
_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]
plt.xticks(list(x)[::3], _xtick_labels[::3], rotation=270)  # rotation旋转的度数

# 添加描述信息
plt.xlabel("时间")
plt.ylabel("温度 单位(℃)")
plt.title("10点到12点每分钟的气温变化情况")

# 绘制网格
plt.grid(alpha=0.4)

plt.savefig("./t2.png")

plt.show()
