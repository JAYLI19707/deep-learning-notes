# References

## Stanford Course Materials

- Stanford CS231N, `reference/stanford/cs231n/modules/cs231n-regularization-optimization.pdf`
- Stanford CS229, `reference/stanford/cs229/bias-variance.pdf`

## Interview Question Sources

- `L1 regularization 和 L2 regularization 的区别是什么？`
  - Confidence label: 经典面试题型
  - Safe wording: 常见于机器学习、算法、数据科学岗位的基础概念题。
- `为什么给 loss 加上 L2 penalty 往往能缓解 overfitting？`
  - Confidence label: 课程高频变体
  - Safe wording: 常见于课程作业变体、公开面经整理和训练原理追问。
- `什么场景下会考虑 L1，而不是默认用 L2？`
  - Confidence label: 课程高频变体
  - Safe wording: 常见于正则化、特征选择和模型可解释性相关追问。

## Figure Mapping

- `concept-intuition`
  - file: `cs231n-regularization-optimization-p20.png`
  - intended page: 第 1 页
  - supports which paragraph: “norm 先是长度，再变成偏好”
  - why this figure is worth choosing: 用“更简单模型 vs 更复杂模型”一眼建立 regularization 的第一层直觉，非常适合概念页开场。
- `problem-motivation`
  - file: `cs229-bias-variance-p23.png`
  - intended page: 第 2 页
  - supports which paragraph: “为什么 regularization 总和 overfitting 绑在一起”
  - why this figure is worth choosing: 它把 model complexity、training error 和 generalization error 放在同一条曲线上，最适合讲动机。
- `mechanism-flow`
  - file: `cs231n-regularization-optimization-p23.png`
  - intended page: 第 3 页
  - supports which paragraph: “regularization 是怎么写进训练目标的”
  - why this figure is worth choosing: 直接把 data loss 和 regularization 放进同一个 objective，最适合讲机制。
- `detail-mechanism`
  - file: `cs231n-regularization-optimization-p25.png`
  - intended page: 第 4 页
  - supports which paragraph: “为什么 regularization 常常会让模型更稳”
  - why this figure is worth choosing: 这一页直接列出了 preference、simplicity、optimization 三条机制线。
- `architecture-overview`
  - file: `cs231n-regularization-optimization-p29.png`
  - intended page: 第 5 页
  - supports which paragraph: “训练目标到底由哪些部分拼出来”
  - why this figure is worth choosing: 它把 score function、data loss、regularization loss 和 full loss 的结构串了起来。
- `application-scene`
  - file: `cs231n-regularization-optimization-p27.png`
  - intended page: 第 6 页
  - supports which paragraph: “为什么 L2 常做默认选项”
  - why this figure is worth choosing: 用同样预测、不同权重形状的例子，直观解释 L2 为何偏好分散且平滑的权重。
- `comparison-tradeoff`
  - file: `cs231n-regularization-optimization-p28.png`
  - intended page: 第 7 页
  - supports which paragraph: “L1 和 L2 到底差在哪”
  - why this figure is worth choosing: 这张图最适合支撑“偏好的权重形状不同”这条核心对比。
- `summary-recap`
  - file: `cs229-bias-variance-p15.png`
  - intended page: 第 10 页
  - supports which paragraph: “为什么不能只盯训练误差”
  - why this figure is worth choosing: 它提醒读者训练误差会随着复杂度持续下降，为最后的收束页提供一个很清晰的收口。

## Slide Capture

- Course: Stanford CS231N
- Module id: `cs231n-regularization-optimization`
- Used pages: 20, 23, 25, 27, 28, 29
- Official source page: `https://cs231n.stanford.edu/2024/schedule.html`
- Exported figures:
  - `episodes/norm-in-ml/images/figures/reference/cs231n-regularization-optimization-p20.png`
  - `episodes/norm-in-ml/images/figures/reference/cs231n-regularization-optimization-p23.png`
  - `episodes/norm-in-ml/images/figures/reference/cs231n-regularization-optimization-p25.png`
  - `episodes/norm-in-ml/images/figures/reference/cs231n-regularization-optimization-p27.png`
  - `episodes/norm-in-ml/images/figures/reference/cs231n-regularization-optimization-p28.png`
  - `episodes/norm-in-ml/images/figures/reference/cs231n-regularization-optimization-p29.png`

## Slide Capture

- Course: Stanford CS229
- Module id: `cs229-bias-variance`
- Used pages: 15, 23
- Official source page: `https://cs229.stanford.edu/notes2022fall/bias-variance.pdf`
- Exported figures:
  - `episodes/norm-in-ml/images/figures/reference/cs229-bias-variance-p15.png`
  - `episodes/norm-in-ml/images/figures/reference/cs229-bias-variance-p23.png`
