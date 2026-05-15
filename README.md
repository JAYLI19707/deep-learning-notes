# 深度学习笔记

从零开始学深度学习，涵盖核心概念、数学原理与代码实践。

## 目录结构

```
├── Pytorch/                # PyTorch 入门教程
├── Norm/                   # L1 / L2 正则化
├── Regularization/         # 正则化综述
├── Dropout/                # Dropout 原理与应用
├── KL_divergence/          # KL 散度与交叉熵
├── attention/              # 注意力机制
├── evaluation metrics/     # 评估指标
└── resample/               # 重采样方法
```

每个文件夹下：
- `fig/` — 配图
- `code/` — 代码与 Notebook
- `*.pdf` — 完整笔记文档
- `*.md` — 补充说明

---

## 内容简介

### Pytorch

从张量操作到自动微分，从构建第一个神经网络到实战训练，手把手带你上手 PyTorch。包含两版笔记和 CS224N、CS231n 配套教程代码。

### Norm — L1 / L2 正则化

回答面试高频问题：L1 和 L2 有什么区别？为什么加 L2 penalty 能缓解过拟合？什么场景用 L1？从"参数大小的度量"讲到"模型偏好的表达"。

### Regularization

正则化方法综述，配合 CS231n 课件，系统梳理训练中防止过拟合的各类手段。

### Dropout

训练时随机丢弃神经元，测试时做模型平均。从"稀疏子网络集成"的视角理解 Dropout，结合 CS231n、CS224N、MIT 6.S191 等课程整理。

### KL 散度

从信息论出发，一次讲透 KL 散度、交叉熵、负对数似然、Softmax + CE、最大似然之间的关系。配合可视化代码，把抽象公式变成直觉。

### Attention

注意力机制图解，包含中英文两个版本的插图，帮助理解 Self-Attention、Multi-Head Attention 的工作原理。

### Evaluation Metrics

评估指标图解，涵盖分类与回归中常用的度量方式。

### Resample

重采样方法图解，理解数据不平衡场景下的采样策略。

---

## 参考课程

- Stanford CS231n: Deep Learning for Computer Vision
- Stanford CS224N: Natural Language Processing with Deep Learning
- Stanford CS229: Machine Learning
- MIT 6.S191: Introduction to Deep Learning

---

## License

本仓库内容仅供学习交流使用。
