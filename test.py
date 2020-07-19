import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(10, 100, size=(2, 5), dtype=int))
#print(df)

df2 = pd.DataFrame(np.random.rand(2, 5) * 100)
print(df2.head())
