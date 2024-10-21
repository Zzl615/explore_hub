# -*- coding: utf-8 -*-
# @Author: Noaghzil
# @Date:   2023-05-20 16:34:49
# @Last Modified by:   Noaghzil
# @Last Modified time: 2023-05-20 16:35:19
import numpy as np

# 模拟数据集
X = np.array([1, 2, 3, 4, 5])   # 输入特征
y = np.array([2, 4, 6, 8, 10])  # 目标变量

# 初始化参数
w = 0.0
b = 0.0
learning_rate = 0.01
num_epochs = 100

# 批量梯度下降优化
for epoch in range(num_epochs):
    # 计算预测值
    y_pred = w * X + b

    # 计算损失函数（均方误差）
    loss = np.mean((y_pred - y) ** 2)

    # 计算梯度
    dw = np.mean(2 * (y_pred - y) * X)
    db = np.mean(2 * (y_pred - y))

    # 更新参数
    w -= learning_rate * dw
    b -= learning_rate * db

    # 打印损失函数
    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss}')

# 输出最优参数
print(f'Optimized parameters: w = {w:.2f}, b = {b:.2f}')
