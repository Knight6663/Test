# -*- coding:UTF-8 -*-
"""
作者:吕瑞承
日期:2021年04月01日14时
"""

from matplotlib import pyplot as plt

# 设置图片大小
fig = plt.figure(figsize=(15, 8), dpi=80)

x = range(2, 26, 2)
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15]

# 绘图
plt.plot(x, y)

# 绘制x轴的刻度
plt.xticks(range(2, 25))
plt.yticks(range(min(y), max(y) + 1))

# 保存
plt.savefig("./t1.png")  # 可以保存为svg这种矢量图格式，放大不会有锯齿

# 展示图形iz
plt.show()
