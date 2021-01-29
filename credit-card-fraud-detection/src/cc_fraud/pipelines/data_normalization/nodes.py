from typing import Dict, Tuple
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def label_encoding(data: pd.DataFrame) -> Tuple[pd.DataFrame, Dict[str, LabelEncoder]]:
    df_cat = data.select_dtypes(include=[object]) 
    df_num = data.select_dtypes(exclude=[object])
    dct = {}
    for col in df_cat.columns:
        le = LabelEncoder()
        df_cat[col] = le.fit_transform(df_cat[col])
        dct[col] = le 
    df = df_cat.join(df_num)
    return df, dct

def label_encoding_test(data: pd.DataFrame, encoders: Dict[str, LabelEncoder]) -> pd.DataFrame:
    df_cat = data.select_dtypes(include=[object]) 
    df_num = data.select_dtypes(exclude=[object])
    for name, enc in encoders.items():
        df_cat[name] = enc.transform(df_cat[name])
    df = df_cat.join(df_num)
    return df
