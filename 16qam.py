import numpy as np
import matplotlib.pyplot as plt

digram = {'11': 3, '10': 1, '01': -1, '00': -3}  # 设置数字和幅度的对应关系
spots = {}  # 放置点

plt.figure()
plt.xlabel('I', loc='right', labelpad=0.1)
plt.ylabel('Q', loc='top', labelpad=0.1)  # 设置坐标轴的文字标签

ax = plt.gca()  # get current axis 获得坐标轴对象

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')  # 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')  # 指定下边的边作为 x 轴 指定左边的边为 y 轴

ax.spines['bottom'].set_position(('data', 0))  # 指定 data 设置的bottom(也就是指定的x轴)绑定到y轴的0这个点上
ax.spines['left'].set_position(('data', 0))

plt.axis([-5, 5, -5, 5])  # 设置坐标的数字范围

for i in ['0', '1']:
    for j in ['0', '1']:
        for k in ['0', '1']:
            for p in ['0', '1']:
                str = ''.join([i, j, k, p])  # 通过循环获得16个4位数的10组合
                str1 = ''.join([i, j])  # 前两个10组合
                a = digram[str1]  # 获取前两个10组合对应的幅值
                # a = int(a)

                str2 = ''.join([k, p])
                b = digram[str2]  # 获取后两个10组合对应的幅值
                # b = int(b)

                complexSpot = complex(a, b)  # 不能写为a+bj，因为编译不通过 生成坐标
                plt.scatter(a, b, c='black')  # 绘制点
                plt.text(a, b + 0.3, str, fontsize=10, color="black", weight="light", verticalalignment='center',
                         horizontalalignment='center', rotation=0)  # 绘制10组合
                tempspot = {str: complexSpot}  # 获得数字组合和点
                spots.update(tempspot)  # 存入点的集合

plt.show()  # 显示图形
plt.savefig('16qam_constellation.png', dpi=300, bbox_inches='tight')