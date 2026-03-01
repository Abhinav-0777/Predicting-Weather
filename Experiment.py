import pandas as pd
# import numpy as np
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# import yaml

# df = pd.read_csv("weatherAUS.csv")
# # missing_per_column = df.isna().sum()
# # print(((missing_per_column/len(df))*100) > 10)
# # num_cols = df.select_dtypes(np.number)
# # print(num_cols.columns)

# # corr_matrix = num_cols.corr()
# # print(corr_matrix[corr_matrix > 0.7])

# X = df[:,:-1]
# print(X)

# with open("config.yaml","r") as file :
#     yaml.safe_load(file)

# data = {"Target":["RainTomorrow"]}

# with open("config.yaml","w") as file :
#     config = yaml.dump(data,file)
# print("Hello")
