import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(20, 80, size=(10, 4)))
df.columns = ['A', 'B', 'C', 'D']
df.columns.value_counts()
