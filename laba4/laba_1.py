import random
import pandas as pd
import numpy as np

df = pd.read_excel('C:/Users/yulia/OneDrive/Docs/Stydy/Avtomatizacia/laba4/rus_dasl16.xls')

def sample_element():
    i = random.randint(5, 2069)
    s = df.iloc[i, 3]
    return s

samples = list()
sizes = [10, 30, 50, 100]

for size in sizes:
    sample = list()
    for sample_num in range(50):
        s = 0
        while s < 18 or s > 25.5:
            s = sample_element()
        sample.append(s)
    samples.append(sample)

means = []
variances = []

# Вычислим оценки для каждой выборки
for sample in samples:
    mean = np.mean(sample)  # Оценка математического ожидания
    variance = np.var(sample, ddof=1)  # Оценка дисперсии (ddof=1 для несмещённой оценки)
    
    means.append(mean)
    variances.append(variance)

# Выведем результаты
for i, (mean, variance) in enumerate(zip(means, variances)):
    print(f"Выборка {i + 1}:")
    print(f"  Оценка математического ожидания: {mean:.4f}")
    print(f"  Оценка дисперсии: {variance:.4f}")
    print()

for mean in means:
    mean_all = np.mean(mean)  # Оценка математического ожидания

for variance in variances:
    variance_all = np.var(variance, ddof=1)  # Оценка дисперсии (ddof=1 для несмещённой оценки)

print (mean_all)

