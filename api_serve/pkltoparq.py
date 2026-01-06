import pandas as pd
import os
print(f"The file to be stored in {os.getcwd()}")
df=pd.read_pickle("../project/movies_list.pkl")
# similarity=pd.read_pickle("../project/similarity_matrix.pkl")
# similarity.to("similarity_matrix.parquet")
df.to_parquet("movies_list.parquet")