# Lean_DataMining
datamining Algorithms

## K_means:(kmeans可以直接运行)
* 用k均值的方法进行聚类
  - 主要函数：
    + 根据分类计算聚类中心
    + 计算两点之间距离
    + 将所有点按照距离中心点的距离进行分类
    + 初始化：创建k个中心点
  - 算法整体思想：见https://blog.csdn.net/qq_36219266/article/details/82657694
## Apriori.py(Learn_Apriori可以直接运行):
* 根据关联规则进行数据挖掘
  - 主要函数：
    + 创建初始候选集
    + 计算支持度
    + 根据支持度筛选小于支持度的
    + 产生候选集
    + 计算置信度
  - 算法整体思想：见https://blog.csdn.net/qq_36219266/article/details/82707708
## FP_Tree算法：
* 根据关联规则进行数据挖掘，找到频繁项集
  - 算法整体思想：https://blog.csdn.net/qq_36219266/article/details/82784299
## AdaBoost Algorithm:
* 整体思想就是根据bagging算法，比如，去看医生，n个医生有n个方法，其中出现次数最多的方法可能是最优解，现在为这些医生赋予权重
  - 算法整体思想：https://blog.csdn.net/qq_36219266/article/details/82799071
  - 现在只是二分类，实际上可以**多分类**，这里属于遗留问题
## CART Algorithm:
* 分类回归树,建立决策树是根据基尼系数的改变量,而后通过后剪枝的过程使得树不要分的太细致
* 参考博客为:https://blog.csdn.net/xiaqunfeng123/article/details/34820095
## ID3 Algorithm
* ID3算法,也是建立决策树,是根据信息熵的增益来建树,而C4.5是信息熵增益比来建树
    
