import pandas as pd
bad_rate_1 = pd.read_csv("E:/mojing/train_val/bad_rate_1.csv")
bad_rate_3 = pd.read_csv("E:/mojing/train_val/bad_rate_3.csv")
bad_rate_5 = pd.read_csv("E:/mojing/train_val/bad_rate_5.csv")
bad_rate_7 = pd.read_csv("E:/mojing/train_val/bad_rate_7.csv")
bad_rate_9 = pd.read_csv("E:/mojing/train_val/bad_rate_9.csv")
bad_rate_11 = pd.read_csv("E:/mojing/train_val/bad_rate_11.csv")
dis_f = pd.read_csv("E:/mojing/adding_feature.csv")
bad_rate = pd.merge(bad_rate_5, bad_rate_7, on="Idx")
bad_rate = pd.merge(bad_rate, bad_rate_9, on="Idx")
bad_rate = pd.merge(bad_rate, bad_rate_11, on="Idx")
bad_rate = pd.merge(bad_rate, bad_rate_1, on="Idx")
bad_rate = pd.merge(bad_rate, bad_rate_3, on="Idx")
bad_rate = pd.merge(bad_rate, dis_f, on="Idx")
bad_rate.to_csv("E:/mojing/train_val/features_add_val.csv", index=False)
