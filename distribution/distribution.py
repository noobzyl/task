# coding : utf-8

import numpy as np

distri = input("请输入分布名(例如正态分布输入“normal”) ")
a = float(input("参数1 "))
b = float(input("参数2(如果没有可以输入任何数) "))
c = int(input("个数 "))

func_dic = {'beta': np.random.beta(a, b, c), 'chisquare': np.random.chisquare(a, c), \
            'binomial': np.random.binomial(int(a), b-int(b), c), 'exponential': np.random.exponential(a, c), \
            'f': np.random.f(a, b, c), 'gamma': np.random.gamma(a, b, c), \
            'normal': np.random.normal(a, b, c), 'poisson': np.random.poisson(a, c), \
            'power': np.random.power(a, c)}

random_list = func_dic[distri]
sample_maximum = np.max(random_list)
sample_minimum = np.min(random_list)
sample_mean = np.mean(random_list)
sample_median = np.median(random_list)
sample_lowquartile = np.percentile(random_list, 25)
sample_highquartile = np.percentile(random_list, 75)
sample_variance = np.var(random_list)
sample_standarddeviation = np.std(random_list, ddof=1)#计算样本标准差，将ddof改成0计算总体标准差
print(f'样本极大值是{sample_maximum}样本极小值是{sample_minimum}\n'
      f'样本中位数是{sample_median}样本均值是{sample_mean}\n'
      f'样本下四分位数是{sample_lowquartile}样本上四分位数是{sample_highquartile}\n'
      f'样本方差是{sample_variance}样本标准差是{sample_standarddeviation}\n')