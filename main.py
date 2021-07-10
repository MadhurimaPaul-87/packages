from functions.an import *
import pandas as pd

data = pd.read_csv("C:\\Users\Madhurima Paul\Downloads\Anova.csv",header=None)
print(data)
print(statistic(data))
print(get_n_k(data))
print(getTreatmentMeans(data))
print(getTotalMean(data))
print(meanOfMeans(data))
print(getSSW(data))
print(getSSB(data))