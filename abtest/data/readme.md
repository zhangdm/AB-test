
## 样本数据

![数据格式](./image/data.png)

包含4列，第一列是uid，每个uid是唯一，也就是说每个uid只有一条记录；
第二列是metric1，第一个指标；第三列是metric2,第二个指标；
第四列是batch，表示实验版本，用以区分是对照组还是实验组的标志。

指标是metric1和metric2两者复合而成，通常是做除法，以metric1做为分子，metric2作为分母，比如metric1 / metric2，代码中以对metric2为0的情况作了删除处理。