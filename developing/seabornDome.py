import seaborn as sns
import numpy as np
if __name__=='__main__':
   sns.set(color_codes=True)
   x=np.random.normal(size=100)
   sns.distplot(x)