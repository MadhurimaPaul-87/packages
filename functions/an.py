import numpy as np


def meanOfMeans(df):
  n = len(df)*len(df.columns)
  s=0
  for i in range(len(df)):
    for j in range(len(df.columns)):
      s= s+ df.loc[i,j]
  return s/n


def get_n_k(df):
  n= len(df)
  k= len(df.columns)
  return n, k

def getTreatmentMeans(df):
  return df.mean()

def getTotalMean(df):
  x = np.array(df)
  n= len(df)
  k= len(df.columns)
  m = n*k
  x= x.reshape(m,1)
  return x.mean()



def getSSB(df):
  if len(df.columns)!= len(df.mean()):
    return "error!!!"
  SSB = 0
  means = df.mean()
  n = len(df)*len(df.columns)
  for i in range(len(df.mean())):
    SSB = SSB + (means[i]-meanOfMeans(df))**2
  return SSB*len(df)

def getSSW(df):
  SSW = 0
  means = df.mean()
  for i in range(len(df.columns)):
    for j in range(len(df)):
      SSW = SSW +(df.loc[j,i]-means[i])**2
  return SSW

def statistic(df):
  n,k = get_n_k(df)
  SSB = getSSB(df)
  SSW = getSSW(df)
  MSB = SSB/(k-1)
  MSW = SSW/(n*k-k)
  return MSB/MSW