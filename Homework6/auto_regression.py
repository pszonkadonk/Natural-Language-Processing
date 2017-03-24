import numpy as np
import pandas as pd
import statsmodels.api as sm
import seaborn as sns

auto_data_df = pd.read_csv('./auto.csv')
sns.set()


X = pd.to_numeric(auto_data_df['horsepower'], errors='coerce')
X = sm.add_constant(X)
y = pd.to_numeric(auto_data_df['mpg'], errors='coerce')



model = sm.OLS(y, X, missing="drop").fit()

print(model.summary())


X = pd.to_numeric(auto_data_df['horsepower'], errors='coerce') # remove constants

sns.regplot(x = X,y = y, data = auto_data_df)

sns.plt.show()

