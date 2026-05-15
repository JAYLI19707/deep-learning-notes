# 为什么往 loss 里加一个 norm，模型就会更稳

## Brief

- 核心问题：把 `L1 / L2 regularization` 讲成一条完整主线，回答“norm 到底是什么、为什么写进 loss 以后会改变模型偏好、为什么 L2 常做默认项、L1 又为什么更容易带来稀疏解”。
- 受众：机器学习 / 算法 / AI 面试准备者，默认按初学者可理解的方式写，不假设读者已经学过优化理论。
- 本期想覆盖的 1-3 个子点：
  - norm 原本是“参数大小的度量”，写进目标函数后就变成了“模型偏好的表达”。
  - regularization 真正限制的不是训练本身，而是模型为了压低训练误差愿意走到多极端。
  - L1 和 L2 的区别重点不在公式表面，而在它们偏好的权重形状、泛化效果和应用场景。
- 候选面试题：
  - L1 regularization 和 L2 regularization 的区别是什么？
  - 为什么给 loss 加上 L2 penalty 往往能缓解 overfitting？
  - 什么场景下会考虑 L1，而不是默认用 L2？
- 需要的模块 refs：
  - `cs231n-regularization-optimization`
  - `cs229-bias-variance`
- 页数策略：`standard = 10 pages`
