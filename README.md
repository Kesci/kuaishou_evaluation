# 快手用户兴趣建模大赛 --- 评审环节
欢迎参加[科赛网](https://www.kesci.com)与快手联合举办的[用户兴趣建模大赛](https://www.kesci.com/apps/home/competition/5ad306e633a98340e004f8d1)。经授权，我们开放此次比赛的评审脚本，供参赛选手在本地环境对个人的模型做验证(validation)。

## 测评指标
此次比赛用到的测评指标为**AUC**，具体详见[Wikipedia](https://en.wikipedia.org/wiki/Receiver_operating_characteristic#Area_under_the_curve)

## 使用方法
* `git clone`仓库到本地
* 运行`python evaluation_script.py submit_file test_file`,submit_file为你的提交，test_file为答案集合

[比赛报名链接](https://www.kesci.com/apps/home/competition/5ab8c36a8643e33f5138cba4/content)