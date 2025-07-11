import numpy as np
import matplotlib.pyplot as plt

bitsToAmp = {'11': 3, '10': 1, '01': -1, '00': -3}  # 设置数字和幅度的对应关系
spots = {}  # 放置点

for i in ['0', '1']:
    for j in ['0', '1']:
        for k in ['0', '1']:
            for p in ['0', '1']:
                strs = ''.join([i, j, k, p])  # 通过循环获得16个4位数的10组合
                str1 = ''.join([i, j])  # 前两个10组合
                a = bitsToAmp[str1]  # 获取前两个10组合对应的幅值
                a = int(a)

                str2 = ''.join([k, p])
                b = bitsToAmp[str2]
                b = int(b)  # 获取后两个10组合对应的幅值

                complexSpot = complex(a, b)  # 不能写为a+bj，因为编译不通过 生成坐标

                tempSpot = {strs: complexSpot}  # 获得数字组合和点
                spots.update(tempSpot)  # 存入点的集合

fig = plt.figure()
t = np.arange(0, 12.0, 0.5)  # 设置基带信号10的坐标轴，每隔0.5的距离绘制一个基带的二进制信号，一共16个比特

# input
plt.subplot(2, 1, 1)
y1 = [0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1]
plt.plot(t, y1, drawstyle='steps-post')  # 将16个比特每隔0.5绘制到坐标系上
plt.xlim(0, 12)
plt.ylim(-0.5, 1.5)
plt.title('16QAM modulation')

# 串并变换
l4 = int(len(y1) / 4)  # 获取比特流的长度除以4，4个比特为一组，则共有多少组
a = np.asarray(y1)  # 将基带信号转换为numpy格式
y2 = a.reshape(l4, 4)  # 将一维数组转置为二维数组，每一行中有4个比特的数据

plt.subplot(2, 1, 2)
t = np.arange(0, 12., 0.01)  # 横坐标的数据列表，每个0.01绘制一个点
rectwav = []  # 用来存储纵坐标值的列表

# i表示第i个线段，每个线段对应一个二进制的四位组合s0s1s2s3。每个线段的长度为2，是基带信号每个信号长度0.5的四倍
for i in range(l4):
    b = y2[i]  # 取出第i组四位数组合s0s1s2s3
    str4Bits = str(b).strip('[').strip(']').replace(' ', '')  # 将列表中的4个比特转换为字符串并且去掉[ ] 和空格
    complexWave = spots[str4Bits]  # 根据四个比特的字符串对应到字典中的复数，得到横坐标和纵坐标的幅度，I Q的幅度值
    xWave = complexWave.real  # 取出横坐标的值
    yWave = complexWave.imag  # 取出纵坐标的值

    # 在t数组中第i段横坐标的点数，此处每个段的波形长度应该是0.5的4倍，也就是2
    t_tmp = t[(i * 200):((i + 1) * 200)]
    xI_tmp = xWave * np.ones(200)  # 200个横坐标的幅度值
    yQ_tmp = yWave * np.ones(200)  # 200个纵坐标的幅度值
    # 将幅度分别与两个正交载波相乘求和
    wav_tmp = xI_tmp * np.cos(2 * np.pi * 5 * t_tmp) - yQ_tmp * np.sin(2 * np.pi * 5 * t_tmp)
    rectwav.append(wav_tmp)  # 将调制后的点加到总的波形列表中

# 绘制调制后的波形
plt.plot(t, np.array(rectwav).flatten())
plt.xlim(0, 12)
plt.ylim(-5, 5)

plt.tight_layout()
plt.savefig('16qam_test.svg', dpi=300, bbox_inches='tight')